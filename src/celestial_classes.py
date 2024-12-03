

class Celestial:
    ''' A base class to represent a celestial body such as a planet, moon or star
    '''
    def __init__(self, name="", primary=None) -> None:
        ''' Initialise the the object with a set of attributes
        '''
        self.name=name
        self.primary = primary
        self.orbiting_objects = []
        
    def __str__(self) -> str:
        ''' Returns the string representation of the object
        '''
        return f"My name is {self.get_name()} and my primary is {self.get_primary().get_name()}."
    
    def get_name(self) -> str:
        ''' Returns the name of the object
        '''
        return self.name
    
    def get_primary(self) -> object:
        ''' Returns the primary object of the object
        '''
        return self.primary
    
    def add_orbiting_objects(self, object_list):
        ''' Enables the adding of orbiting objects to the [this] primary object
        '''
        self.orbiting_objects.extend(object for object in object_list)
    
    def get_orbiting_objects(self) -> list:
        ''' Returns a list of the orbiting objects
        '''
        return self.orbiting_objects
    
    def get_orbiting_objects_names(self, return_type) -> list:
        ''' Returns the names of the orbiting objects. Can be requested as a list or a string.
            If an object has no orbiting objects, a string "None" is returned
        '''
        try:
            if len(self.get_orbiting_objects()) > 0:
                if return_type == "list":
                    return [object.get_name() for object in self.get_orbiting_objects()]
                elif return_type == "string":
                    return ', '.join(object.get_name() for object in self.get_orbiting_objects())
            else:
                return "None"
        except:
            return None
    
    def get_num_orbiting_objects(self) -> int:
        ''' Returns the number of orbiting objects for a given Primary
        '''
        return len(self.get_orbiting_objects())
        

class Star(Celestial):
    ''' A class to represent a star, inheriting from Celestial class.
    '''
    def __init__(self, name="") -> None:
        ''' Initialises the star with a name
        '''
        super().__init__(name)
        
    def __str__(self) -> str:
        ''' Returns the string representation of the object
        '''
        return f"My name is {self.get_name()} and I have {self.get_orbiting_objects_names('string')} in my orbit"
    
    
class Planet(Celestial):
    ''' A class to represent a planet, inheriting from Celestial class.
    '''
    def __init__(self, name="", primary=None, mass=0.0, distance=0.0, rotational=0.0, fact1="", fact2="") -> None:
        ''' Initialises the planet with several attributes
        '''
        super().__init__(name, primary)
        self.mass = mass
        self.distance = distance
        self.rotational = rotational
        self.facts = [fact1, fact2]
        
    def __str__(self) -> str:
        ''' Returns the string representation of the object
        '''
        return (f"My name is {self.get_name()}. "
                f"I orbit {self.get_primary().get_name()}. "
                f"My mass is {self.get_mass()} e+24 kg. "
                f"My distance from {self.get_primary().get_name()} is {self.get_distance()} million km. "
                f"My rotational speed is {self.get_rotational()} m/s. "
                f"2 key facts about me are: "
                f"Fact 1: {self.get_facts()[0]} "
                f"Fact 2: {self.get_facts()[1]} "
                f"I have {self.get_num_orbiting_objects()} moons in my orbit. "
                f"My moons are: {self.get_orbiting_objects_names('string')}."
        )
    
    def get_mass(self) -> float:
        ''' Returns the mass of the object in e+24kg
        '''
        return self.mass
    
    def get_distance(self) -> float:
        ''' Returns the distance (from the sun/star) of the object in millions of km
        '''
        return self.distance
    
    def get_rotational(self) -> float:
        ''' Returns the rotational speed in m/s of the object
        '''
        return self.rotational
    
    def get_facts(self) -> list:
        ''' Returns a list of facts relating to the object'''
        return self.facts
    


class Moon(Celestial):
    ''' A class to represent a moon, inheriting from Celestial class.
    '''
    def __init__(self, name="", primary=None) -> None:
        ''' Initialises a moon with attributes
        '''
        super().__init__(name, primary)
        
    def __str__(self) -> str:
        ''' Returns a string representation of the object
        '''
        return super().__str__()
        

        
        
        