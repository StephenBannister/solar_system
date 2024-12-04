import logging
from .celestial_classes import Star, Planet, Moon
from .load_json import load_json_data


def create_star(name):
    ''' Creates and returns a star object with a name
    '''
    s = Star(name)
    return s
    
def create_planets(star):
    ''' Create planet objects from JSON data and add them to the star object.
        If a planet name already exists for the Star, then it is ignored and a warning logged.
        If the JSON file is incorrectly formatted or the data is incorrect an exception is raised.
    '''
    try:    
        filename = "config/planets.json"
        planet_data = load_json_data(filename)
        
        for planet in planet_data:
            planet_name = planet["name"]
            if planet["name"] in star.get_orbiting_objects_names('list'):
                logging.warning(f"Planet {planet_name} from {filename} already exists in {star.get_name()}'s orbiting objects. The duplicate name has been ignored.")
                continue
            else:
                new_planet = Planet(name=planet["name"], primary=star, mass=planet["mass"], distance=planet["distance"], rotational=planet["rotational"], fact1=planet["fact1"], fact2=planet["fact2"])
                star.add_orbiting_objects(new_planet)
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid planet in data structure from {filename}")
    except Exception as e:
        logging.error(f"Failed to create planets {e}")
        raise
        
        

def create_moons(star):
    ''' Create moon objects from JSON data and add them to the respective planet objects.
        If a moon name already exists for the Planet, then it is ignored and a warning logged.
        If the JSON file is incorrectly formatted or the data is incorrect an exception is raised.
    '''
    try:
        filename = "config/moons.json"
        moon_data = load_json_data(filename)
        
        for planet in star.get_orbiting_objects():
            moon_names = moon_data.get(planet.get_name(), [])
            for moon_name in moon_names:
                if moon_name in planet.get_orbiting_objects_names('list'):
                    logging.warning(f"Moon {moon_name} already exists in {planet.get_name()}'s orbiting objects. The duplicate name has been ignored.")
                    continue
                else:
                    planet.add_orbiting_objects(Moon(moon_name, planet))                
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid moon in data structure in {filename}")
    except Exception as e:
        logging.error(f"Failed to create moons {e}")
        raise
    
        
def run_creation():
    ''' Consolidator function to create the objects for the solar system and return the star
    '''
    s = create_star("Sun")
    create_planets(s)
    create_moons(s)
    print("Solar System Created Successfully")
    return s

    
    
    