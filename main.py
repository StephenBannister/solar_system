
"""
This is the main script used to start all the processes to model a basic solar system with stars, planets, and moons.

Key references used in the coding of this application:
    - Gray, D (2023), Python Tutorial for Beginners (with mini-projects), free CodeCamp. https://youtu.be/qwAFL1597eM?si=1DQAWVE6F4FlF4zc
    - Spronk, P. (2023), The Coder's Apprentice. https://www.spronck.net/pythonbook/
    - Downey, A. (2012), Think Python: How to Think Like a Computer Scientist: Learning with Python 3, Greentea Press. http://www.thinkpython.com
    - Real Python, 2024. Composition in Python. [online video] Available at: https://realpython.com/videos/composition/
    - Real Python, 2024. Inheritance in Python. [online video] Available at: https://realpython.com/videos/inheritance-python/
    - GeeksforGeeks, 2024. Python super(). [online] Available at: https://www.geeksforgeeks.org/python-super/
    - Python Software Foundation, 2024. unittest — Unit testing framework. [online] Available at: https://docs.python.org/3/library/unittest.html
    - Python Software Foundation, 2024. unittest.mock — mock object library. [online] Available at: https://docs.python.org/3/library/unittest.mock.html
    - Stack Overflow, 2024. Reading JSON from a file. [online] Available at: https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    - W3Schools, 2024. Python JSON. [online] Available at: https://www.w3schools.com/python/python_json.asp
    - GeeksforGeeks, 2024. Read JSON file using Python. [online] Available at: https://www.geeksforgeeks.org/read-json-file-using-python/
    - Python Software Foundation, 2024. PEP 257 — Docstring Conventions. [online] Available at: https://peps.python.org/pep-0257/
    - Python Software Foundation, 2024. PEP 3107 — Function Annotations. [online] Available at: https://peps.python.org/pep-3107/
    - Stack Overflow, 2024. Where can I find proper examples of the PEP 257 docstring conventions?. [online] Available at: https://stackoverflow.com/questions/10017776/where-can-i-find-proper-examples-of-the-pep-257-docstring-conventions
    - Stack Overflow, 2024. What is the best way to structure a Tkinter application?. [online] Available at: https://stackoverflow.com/questions/17466561/what-is-the-best-way-to-structure-a-tkinter-application
    - Python Software Foundation, 2024. Using ttk. [online] Available at: https://docs.python.org/3/library/tkinter.ttk.html#using-ttk
    - Stack Overflow, 2024. How to pass arguments to a button command in Tkinter?. [online] Available at: https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    - Reddit, 2024. In Tkinter, is it OK to add root.mainloop() at the end of a class?. [online] Available at: https://www.reddit.com/r/learnpython/comments/urh4st/in_tkinter_is_it_ok_to_add_rootmainloop_at_the/
    - Stack Overflow, 2024. How to clear the Entry widget after a button is pressed in Tkinter?. [online] Available at: https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
    - W3Schools, 2024. Python Exceptions. [online] Available at: https://www.w3schools.com/python/python_ref_exceptions.asp
    - GeeksforGeeks, 2024. JSON parsing errors in Python. [online] Available at: https://www.geeksforgeeks.org/json-parsing-errors-in-python/
    - Python Software Foundation, 2024. logging — Logging facility for Python. [online] Available at: https://docs.python.org/3/library/logging.html
    - Stack Overflow, 2024. How do I bind the Enter key to a function in Tkinter?. [online] Available at: https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter
    - Stack Overflow, 2024. How do I set focus to an Entry widget from a function?. [online] Available at: https://stackoverflow.com/questions/20792183/how-do-i-set-focus-to-an-entry-widget-from-a-function
    - GeeksforGeeks, 2024. How to Use Images as Backgrounds in Tkinter. [online] Available at: https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
    - Stack Overflow (2015) Play animations in GIF with Tkinter. Available at: https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
    - Stack Overflow, 2024. Explain the setUp() and tearDown() Python methods used in test cases. [online] Available at: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases
    - Python Discussion Forum, 2024. Deleting an object. [online] Available at: https://discuss.python.org/t/deleting-an-object/17299/2
    - Python Software Foundation, 2024. unittest.mock.Mock — Mock class. [online] Available at: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
    - Python Discussion Forum, 2024. Is this desirable that a module is loaded twice?. [online] Available at: https://discuss.python.org/t/is-this-desirable-that-a-module-is-loaded-twice/31196/5
"""

import logging, sys
from src.create_objects import run_creation
from src.menu import create_menu



if __name__ == "__main__":
    ''' It all starts here. Calls the solar system creation function and starts the menu
    '''
    
    try:
        s = run_creation()
    except Exception as e:
        logging.critical(f"Critical error creating solar system {e}")
        sys.exit(1)
    
    create_menu(s)
