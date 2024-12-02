from tkinter import *
from tkinter import ttk, PhotoImage, messagebox
import tkinter as tk
from .system_ui import *
from .load_json import load_json_data


def determine_menu_choice(user_input, s, nlp_matches):
    ''' Function to determine if a user entered the name of a planet and what their menu choice is
    '''
        # Compare the user's input to the names of planets in the solar system to see if there's a match
    planets = [planet for planet in s.get_orbiting_objects()]
    for planet in planets:
        if planet.get_name().lower() in user_input:
            planet_choice = planet
            break
    else:
        planet_choice = None

    # Determine if a single word is entered by the user that is the name of a planet
    if len(user_input.split()) < 2 and planet_choice is not None:
        menu_choice = 1  # Default to the menu choice showing the information related to that planet only
    else:
        # Determine if the user input one of our nlp matches
        for option, keywords in nlp_matches.items():
            if any(keyword in user_input for keyword in keywords):
                menu_choice = int(option)
                break
            else:
                menu_choice = 0
                
    return menu_choice, planet_choice

def process_choices(s, root, scrollable_frame, entry):
    ''' Function to process the menu options and initiate the function to displacy what they want to see.
    '''
    
    # Determine if the user input something and if so, put the user's input into a variable we can use
    user_input=entry.get().lower()
    entry.delete(0, tk.END)
    if not user_input.strip():
        messagebox.showerror("Error", "Input cannot be blank. Please enter a valid request.")
        return
    
    # Get JSON file dictionary content of possible word matches for each option
    nlp_file = "config/nlp_choices.json"
    nlp_matches = load_json_data(nlp_file)
    
    menu_choice, planet_choice = determine_menu_choice(user_input, s, nlp_matches)

    # Apply the user's input to an outcome
    if menu_choice == 1:
        clear_frame(scrollable_frame)
        display_planet(scrollable_frame, planet_choice)
    elif menu_choice == 2:
        clear_frame(scrollable_frame)
        display_mass(scrollable_frame, planet_choice)
    elif menu_choice == 3:
        clear_frame(scrollable_frame)
        display_exists(scrollable_frame, planet_choice)
    elif menu_choice == 4:
        clear_frame(scrollable_frame)
        display_moons(scrollable_frame, planet_choice)
    elif menu_choice == 5:
        clear_frame(scrollable_frame)
        display_all(s, scrollable_frame)
    elif menu_choice ==6:
        clear_frame(scrollable_frame)
        display_help(scrollable_frame)
    elif menu_choice == 7:
        root.destroy()
    else:
        messagebox.showerror("Error", "I don't understand your request. Please try again.")
        return


def create_menu(s):
    ''' Function to set up the root window, frames and cards 
        plus display the messages and buttons for the menu
    '''
    # Instantiate root window
    root=Tk()
    root.geometry("770x660")
    root.title("The Solar System")
    root.configure(background="black")
    
    bg1 = tk.PhotoImage(file="images/earth.png")
    bg2 = tk.PhotoImage(file="images/moon.png")
    
    # Setup styles
    style = ttk.Style()
    style.configure("1.TFrame", foreground="white", background="black")
    style.configure("1.TLabel", foreground="white", background="black")
    style.configure("TButton", padding=1, relief="flat", background="#ccc")
    
    # Instantiate frames, cards image label and input fields
    frame_title = ttk.Frame(root, height = 50, padding=10, style="1.TFrame")
    frame_input = ttk.Frame(root, height = 80, padding=10, style="1.TFrame")
    #frame_input = ttk.Frame(root, height = 80, padding=10, style="1.TFrame", relief="ridge")
    entry = ttk.Entry(frame_input, width=50)    
    frame_display = ttk.Frame(root, height=200, padding=10)
   
    label1 = Label(frame_title, image=bg2, background = "black")
    label1.place(x = 550, y =-100)

    label2 = Label(frame_input, image=bg1, background = "black")
    label2.place(x = 0, y =0)
   
    # Create a canvas and scrollbar for the scrollable frame
    canvas = Canvas(frame_display)
    scrollbar = ttk.Scrollbar(frame_display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create the scrollable frame
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Place the scrollable frame in the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Pack the canvas and scrollbar in frame_display
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Pack frames and cards into respective windows
    frame_title.pack(fill="both", expand=False)
    frame_input.pack(fill="both", expand=False)        
    frame_display.pack(fill="both", expand=True)
    
    #tk.Label(frame_input, image=gfg_picture, anchor="e").pack()
    
    ttk.Label(frame_title, text="Hello Solar Explorer", font=("Arial", 14, "bold"), style="1.TLabel").pack(pady=5)
    ttk.Label(frame_input, text="Please enter your query, or ask for help:", font=("Arial", 12), style="1.TLabel").pack(pady=5)

    # Automatically put the cursor in the entry field
    entry.focus()

    # Ensure the Enter key submits the input
    root.bind("<Return>", lambda event: process_choices(s, root, scrollable_frame, entry))

    entry.pack(pady=5)
    
    ttk.Button(frame_input, text="Submit", command=lambda: process_choices(s, root, scrollable_frame, entry), style="TButton").pack(pady=10)
    ttk.Button(root, text="Exit", command=root.destroy, style="TButton").pack(pady=10)
    
    root.mainloop()
