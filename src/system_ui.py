from tkinter import *
from tkinter import ttk
import tkinter as tk


def clear_frame(frame) -> None:
    ''' Clears all widgets from the frame.
    '''

    for widget in frame.winfo_children():
        widget.destroy()


def get_labels(planet) -> list:
    ''' Return a list of strings
    '''
    return [    
        f"Name: {planet.get_name()}",
        f"Orbits: {planet.get_primary().get_name()}",
        f"Mass: {planet.get_mass()} x 10^24 kg",
        f"Distance from Sun: {planet.get_distance()} million km",
        f"Rotational speed: {planet.get_rotational()} m/s",
        f"Fact 1: {planet.get_facts()[0]}",
        f"Fact 2: {planet.get_facts()[1]}",
        f"Number of moons: {planet.get_num_orbiting_objects()}",
        f"Moon names: {planet.get_orbiting_objects_names('string')}",
    ]
    
def display_planet(scrollable_frame, planet) -> None:
    ''' Displays a card for the information passed to it e.g. planets
    ''' 
    if planet is not None:
        card = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
        card.pack(fill="x", pady=5)
        
        # Create a PhotoImage and attach it to a label in the card to keep a reference
        planet_picture = tk.PhotoImage(file=f"images/{planet.get_name().lower()}.png")
        card.image = planet_picture
        tk.Label(card, image=planet_picture, anchor="e", pady=2).pack()
        
        labels = get_labels(planet)
        for item in labels:
            if item[:10] == "Moon names" and len(planet.get_orbiting_objects()) == 0:
                continue
            ttk.Label(card, text=item, wraplength=700, justify="left").pack(anchor="w", pady=2)

    else:
        display_message = "The planet you have asked for doesn't exist or cannot be found. Please try again."
        ttk.Label(scrollable_frame, text=display_message, wraplength=650, justify="left").pack(anchor="w", pady=2)
        
    
def display_mass(scrollable_frame, planet) -> None:
    ''' Displays a message about the mass of a planet
    '''
    if planet is not None:
        display_message = f"The mass of {planet.get_name()} is {planet.get_mass()} 10^24 kg"
    else:
        display_message = "The planet you have asked for doesn't exist or cannot be found. Please try again."
        
    ttk.Label(scrollable_frame, text=display_message, wraplength=650, justify="left").pack(anchor="w", pady=2)
        

def display_exists(scrollable_frame, planet) -> None:
    ''' Displays a message about the existence of a planet
    '''
    if planet is not None:
        display_message = f"The planet {planet.get_name()} does indeed exist!" 
    else:
        display_message = "The planet you have asked for doesn't exist or cannot be found. Please try again."
        
    ttk.Label(scrollable_frame, text=display_message, wraplength=650, justify="left").pack(anchor="w", pady=2)
    
    
def display_moons(scrollable_frame, planet) -> None:
    ''' Displays the moons of a planet
    '''
    if planet is not None:
        if planet.get_num_orbiting_objects() > 0:
            display_message = f"The planet {planet.get_name()} has {planet.get_num_orbiting_objects()} moons. They are {planet.get_orbiting_objects_names('string')}."
        else:
            display_message = f"The planet {planet.get_name()} has no moons."
    else:
        display_message = "The planet you have asked for doesn't exist or cannot be found. Please try again."
    
    ttk.Label(scrollable_frame, text=display_message, wraplength=650, justify="left").pack(anchor="w", pady=2)
    
    
def display_all(s, scrollable_frame) -> None:
    ''' Displays all the information about all the planets
    '''
    for planet in s.get_orbiting_objects():         
            display_planet(scrollable_frame, planet)
    

def display_help(scrollable_frame) -> None:
    ''' Displays helpful hints on how to use the program
    '''
    display_message = (
        f"Hello and welcome to the Solar System Program Help\n\n"
        f"The Solar System Program allow you to discover many things about the planets in our solar system.\n\n"
        f"This program accepts free text input. You can type what you want to see and if I have that information I will display it.\n\n"
        f"Examples of what you can ask for are:\n\n"
        f"  - 'tell me about Earth'\n"
        f"  - 'show me everything'\n"
        f"  - 'what is the mass of Jupiter'\n"
        f"  - 'how many moons does Saturn have'\n"
        f"  - 'does pluto exist'\n"
        f"  - 'bye' or 'exit' if you've learnt enough\n\n"
        f"Try it out and enjoy learning more about our solar system!"
        )
    ttk.Label(scrollable_frame, text=display_message, wraplength=650, justify="left").pack(anchor="w", pady=2)