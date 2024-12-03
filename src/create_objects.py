import logging
from .celestial_classes import Star, Planet, Moon
from .load_json import load_json_data


def create_star(name):
    ''' Creates and returns a star object with a name
    '''
    s = Star(name)
    return s
    
def create_planets(star):
    ''' Create planet objects from JSON data and add them to the solar system.
    '''
    try:
        filename = "config/planets.json"
        planet_data = load_json_data(filename)
        planets = [Planet(name=item["name"], primary=star, mass=item["mass"], distance=item["distance"], rotational=item["rotational"], fact1=item["fact1"], fact2=item["fact2"]) for item in planet_data]
        star.add_orbiting_objects(planets)
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid moon in data structure in {filename}")
    except Exception as e:
        logging.error(f"Failed to create moons {e}")
        raise
        
        

def create_moons(star):
    ''' Create moon objects from JSON data and add them to the respective planet objects.
    '''
    try:
        filename = "config/moons.json"
        moon_data = load_json_data(filename)
        for planet in star.get_orbiting_objects():
            moon_names = moon_data.get(planet.get_name(), [])
            planet.add_orbiting_objects([Moon(name, planet) for name in moon_names])
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid planet in data structure in {filename}")
    except Exception as e:
        logging.error(f"Failed to create planets {e}")
        raise
    
        
def run_creation():
    ''' Consolidator function to create the objects for the solar system and return the star
    '''
    s = create_star("Sun")
    create_planets(s)
    create_moons(s)
    print("Solar System Created Successfully")
    return s

    
    
    