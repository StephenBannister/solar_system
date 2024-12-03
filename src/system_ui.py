from tkinter import *
from tkinter import ttk
import tkinter as tk
import os


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

def update(ind, frames, label, scrollable_frame):
    ''' Manages each frame of the gif.
    '''
    # Included so we don't get errors when clearing the display after showing an planet
    if not label.winfo_exists():  # Check if the label widget exists
        return  # Stop the animation if the label has been destroyed
    
    frame = frames[ind]
    ind += 1
    if ind == len(frames):  # Use the length of frames to determine when to loop
        ind = 0
    label.configure(image=frame)
    scrollable_frame.after(100, update, ind, frames, label, scrollable_frame)

  
def display_planet(scrollable_frame, planet) -> None:
    ''' Displays a card with a grid for the information passed to it e.g. planets
    ''' 
    if planet is not None:
        card = ttk.Frame(scrollable_frame, padding=10, relief="ridge")
        card.pack(fill="x", pady=5)

        # Set up a grid so our planet gifs/png's display more in line with the text        
        display_grid = ttk.Frame(card)
        display_grid.grid(row=0, column=0, sticky="snew")

        
        # check if a gif exists for the planet, if so, display it, otherwise show a png
        gif_path = f"images/{planet.get_name().lower()}.gif"
        if not os.path.exists(gif_path):
            # Create a PhotoImage and attach it to a label in the card to keep a reference
            planet_picture = tk.PhotoImage(file=f"images/{planet.get_name().lower()}.png")
            card.image = planet_picture
            label = tk.Label(display_grid, image=planet_picture).grid(row=0, column=1, rowspan=10, sticky="nw", padx=5)
            # label.pack(anchor="e", pady=0)
        else:
            # Dynamically determine the number of frames in the GIF, use try, except erroring to control end of frames
            frames = []
            i = 0
            while True:
                try:
                    frame = PhotoImage(file=gif_path, format=f'gif -index {i}')
                    frames.append(frame)
                    i += 1
                except TclError:
                    break  # End of GIF frames
            
            label = tk.Label(display_grid)
            label.grid(row=0, column=1, rowspan=10, sticky="nw", padx=5)
        
            # Call the function to animate the GIF
            update(0, frames, label, scrollable_frame)
        
        # Add text labels for planet information
        labels = get_labels(planet)
        for index, item in enumerate(labels):
            if item.startswith("Moon names") and len(planet.get_orbiting_objects()) == 0:
                continue
            ttk.Label(display_grid, text=item, wraplength=700, justify="left").grid(row=index, column=0, sticky="w", pady=2)

    else:
        # Handle case where the planet does not exist
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