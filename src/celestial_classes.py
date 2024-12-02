

class Celestial:
    def __init__(self, name="", primary=None) -> None:
        self.name=name
        self.primary = primary
        self.orbiting_objects = []
        
    def __str__(self) -> str:
        return f"My name is {self.get_name()} and my primary is {self.get_primary().get_name()}."
    
    def get_name(self) -> str:
        return self.name
    
    def get_primary(self) -> object:
        return self.primary
    
    def add_orbiting_objects(self, object_list):
        self.orbiting_objects.extend(object for object in object_list)
    
    def get_orbiting_objects(self) -> list:
        return self.orbiting_objects
    
    def get_orbiting_objects_names(self, return_type) -> list:
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
        return len(self.get_orbiting_objects())
        

class Star(Celestial):
    def __init__(self, name="") -> None:
        super().__init__(name)
        
    def __str__(self) -> str:
        return f"My name is {self.get_name()} and I have {self.get_orbiting_objects_names('string')} in my orbit"
    
    
class Planet(Celestial):
    def __init__(self, name="", primary=None, mass=0.0, distance=0.0, rotational=0.0, fact1="", fact2="") -> None:
        super().__init__(name, primary)
        self.mass = mass
        self.distance = distance
        self.rotational = rotational
        self.facts = [fact1, fact2]
        
    def __str__(self) -> str:
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
        return self.mass
    
    def get_distance(self) -> float:
        return self.distance
    
    def get_rotational(self) -> float:
        return self.rotational
    
    def get_facts(self) -> list:
        return self.facts
    


class Moon(Celestial):
    def __init__(self, name="", primary=None) -> None:
        super().__init__(name, primary)
        
    def __str__(self) -> str:
        return super().__str__()
        

        
        
        