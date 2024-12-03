""" References used (move to main.py when complete):
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
    - Stack Overflow, 2024. Explain the setUp() and tearDown() Python methods used in test cases. [online] Available at: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases
    - Python Discussion Forum, 2024. Deleting an object. [online] Available at: https://discuss.python.org/t/deleting-an-object/17299/2
    - Python Software Foundation, 2024. unittest.mock.Mock — Mock class. [online] Available at: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
    - Python Discussion Forum, 2024. Is this desirable that a module is loaded twice?. [online] Available at: https://discuss.python.org/t/is-this-desirable-that-a-module-is-loaded-twice/31196/5
"""

''' Git commit notes:



'''
import sys, os, unittest, json

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.celestial_classes import Celestial, Star, Planet, Moon
from src.load_json import load_json_data
from src.menu import determine_menu_choice


class CelestialSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.star = Star("Sun")
        self.earth = Planet(name="Earth", primary=self.star, mass=5.97, distance=149.6, rotational=1670, fact1="I have life.", fact2="I have tectonic plates.")
        self.jupiter = Planet(name="Jupiter", primary=self.star, mass=1898, distance=778.5, rotational=12600, fact1="I an huge.", fact2="I have a giant storm.")
        self.the_moon = Moon(name="The Moon", primary=self.earth)
        self.io = Moon(name="Io", primary=self.jupiter)
    
    

    def tearDown(self) -> None:
        ''' Releases resources that were being used by the test framework
        '''
        self.star = None
        self.earth = None
        self.jupiter = None
        self.the_moon = None
        self.io = None
        

# ---------------- Test Celestial ------------------

    #Test Plan Reference: Core_001
    def test_celestial_name(self):
        celestial_body = Celestial(name="TestBody")
        self.assertEqual(celestial_body.get_name(), "TestBody", "Celestial is not returning the correct name.")

# ---------------- Test Star ------------------
    #Test Plan Reference: Core_002
    def test_star_name(self):
        self.assertEqual (self.star.get_name(), "Sun", "Star is not returning the correct name.")

    #Test Plan Reference: Core_003
    def test_star_add_orbiting_objects(self): 
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        self.assertCountEqual (self.star.get_orbiting_objects(), [self.earth, self.jupiter], "Star is not returning the correct orbiting objects.")
        self.assertEqual (self.star.get_num_orbiting_objects(), 2, "Star is not returning the correct number of orbiting objects.")
        self.assertCountEqual (self.star.get_orbiting_objects_names('string'), "Earth, Jupiter", "Star is not returning the correct orbiting object names.")                


# ---------------- Test Planet ------------------
    #Test Plan Reference: Core_004
    def test_planet_properties(self):
        
        expected_output = (        
            f"My name is Earth. I orbit Sun. My mass is 5.97 e+24 kg. "
            f"My distance from Sun is 149.6 million km. My rotational speed is 1670 m/s. "
            f"2 key facts about me are: Fact 1: I have life. Fact 2: I have tectonic plates. "
            f"I have 1 moons in my orbit. My moons are: The Moon."
        )
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertEqual (self.earth.get_name(), "Earth", "Planet is not returning the correct name.")
        self.assertEqual (self.earth.get_mass(), 5.97, "Planet is not returning the correct mass.")
        self.assertEqual (self.earth.get_distance(), 149.6, "Planet is not returning the correct distance.")
        self.assertEqual (self.earth.get_rotational(), 1670, "Planet is not returning the correct rotational speed.")
        self.assertEqual (self.earth.get_primary().get_name(), "Sun", "Planet is not returning the correct primary name.")
        self.assertEqual (str(self.earth), expected_output, "Planet is not returning the correct string representation.")
    
    #Test Plan Reference: Core_005
    def test_planet_add_orbiting_objects(self):
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not processing the correct add_orbiting_objects result.")
        self.assertCountEqual (self.earth.get_orbiting_objects(), [self.the_moon], "Planet is not returning the correct orbiting objects.")
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not returning the correct number of orbiting objects.")
        self.assertEqual (self.earth.get_orbiting_objects_names('string'), "The Moon", "Planet is not returning the correct orbiting object names.")
    
# ---------------- Test Moon ------------------
    #Test Plan Reference: Core_006
    def test_moon_properties(self):
        self.assertEqual (self.io.get_name(), "Io", "Moon is not returning the correct name.")
        self.assertEqual (self.the_moon.get_name(), "The Moon", "Moon is not returning the correct name.")
        self.assertEqual (self.io.get_primary().get_name(), "Jupiter", "Moon is not returning the correct primary name.")
        self.assertEqual(self.the_moon.get_primary().get_name(), "Earth", "Moon is not returning the correct primary name.")
        
        
# ---------------- Test Object Relationships ------------------
    #Test Plan Reference: Core_007
    def test_object_relationships(self):
        self.star.add_orbiting_objects([self.earth])
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertIn(self.earth, self.star.get_orbiting_objects(), "The relationship between Planet and Star is not correct")
        self.assertIn(self.the_moon, self.earth.get_orbiting_objects(), "The relationship between the Moon and Planet is not correct")
        


# ---------------- Test Edge Cases ------------------

    #Test Plan Reference: Core_008
    def test_empty_orbiting_objects(self):
        celestial_body = Celestial("All_alone")
        self.assertEqual(celestial_body.get_orbiting_objects(), [], "An empty orbiting objects property causes an error")
        self.assertEqual(celestial_body.get_orbiting_objects_names('string'), "None", "An empty orbiting objects names property causes an error")


       
class FileOperationsTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        ''' Releases resources that were being used by the test framework
        '''
        pass

# ---------------- Test JSON File Operations ------------------
    #Test Plan Reference: File_001
    def test_load_json_valid(self):
        data = load_json_data("config/planets.json")
        self.assertIsInstance(data, list, "List not created")
        self.assertTrue(any("Earth" in item["name"] for item in data), "JSON file not loaded correctly")

    #Test Plan Reference: File_002
    def test_load_json_invalid(self):
        with self.assertRaises(FileNotFoundError):
            load_json_data("DoesntExist.json")



class MenuOperationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.star = Star("Sun")
        self.earth = Planet(name="Earth", primary=self.star)
        self.mars = Planet(name="Mars", primary=self.star)
        self.venus = Planet(name="Venus", primary=self.star)
        self.star.add_orbiting_objects([self.earth, self.mars, self.venus])
        self.nlp_matches = load_json_data("tests/test_nlp_choices.json")
    
    def tearDown(self) -> None:
        self.star = None
        self.earth = None
        self.mars = None
        self.nlp_matches = None
    
# ---------------- Menu Choice NLP and Logic ------------------  

    #Test Plan Reference: Menu_001    
    def test_check_menu_choice_valid_sentence_is_all_planet_info(self):
        menu_choice, planet_choice = determine_menu_choice("tell me about earth", self.star, self.nlp_matches)
        self.assertEqual (menu_choice, 1, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice.get_name(), "Earth", "the planet chosen is incorrect")
    
    #Test Plan Reference: Menu_002
    def test_check_menu_choice_valid_name_is_all_planet_info(self):
        menu_choice, planet_choice = determine_menu_choice("venus", self.star, self.nlp_matches)
        self.assertEqual (menu_choice, 1, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice.get_name(), "Venus", "the planet chosen is incorrect")

        
    #Test Plan Reference: Menu_003
    def test_check_menu_choice_valid_sentence_is_planet_mass(self):
        menu_choice, planet_choice = determine_menu_choice("What is the mass of mars", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 2, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice.get_name(), "Mars", "the planet chosen is incorrect")
        
        
    #Test Plan Reference: Menu_004
    def test_check_menu_choice_valid_sentence_is_planet_exist(self):
        menu_choice, planet_choice = determine_menu_choice("does earth exist", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 3, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice.get_name(), "Earth", "the planet chosen is incorrect")    
        
    #Test Plan Reference: Menu_005
    def test_check_menu_choice_valid_sentence_is_planet_moons(self):
        menu_choice, planet_choice = determine_menu_choice("how many moons does earth have", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 4, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice.get_name(), "Earth", "the planet chosen is incorrect")    
        
    #Test Plan Reference: Menu_006
    def test_check_menu_choice_valid_sentence_is_everything(self):
        menu_choice, planet_choice = determine_menu_choice("tell me everything", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 5, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice, None, "the planet chosen is not None")
        
    #Test Plan Reference: Menu_007
    def test_check_menu_choice_valid_sentence_is_help(self):
        menu_choice, planet_choice = determine_menu_choice("help me", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 6, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice, None, "the planet chosen is not None")
 
    #Test Plan Reference: Menu_008
    def test_check_menu_choice_valid_sentence_exit_program(self):
        menu_choice, planet_choice = determine_menu_choice("bye", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 7, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice, None, "the planet chosen is not None")

    #Test Plan Reference: Menu_009
    def test_check_menu_choice_valid_non_matched_input(self):
        menu_choice, planet_choice = determine_menu_choice("this is unmatched", self.star, self.nlp_matches)        
        self.assertEqual (menu_choice, 0, "The choice for the menu is incorrect")
        self.assertEqual (planet_choice, None, "the planet chosen is not None")
        
          
class ErrorHandlingTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        """ Releases resources that were being used by the test framework
        """
        pass
   
   
    #Test Plan Reference: EH_003
    def test_load_json_malformed(self):
        with self.assertRaises(json.JSONDecodeError):
            load_json_data("tests/moons_malformed.json")
    

if __name__ == "__main__":
    unittest.main()