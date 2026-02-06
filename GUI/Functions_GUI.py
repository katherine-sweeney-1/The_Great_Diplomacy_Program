import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
from Functions_Coordinates import assign_coordinates_to_nodes
import math
import numpy as np
from Functions_Drawing import draw_units, draw_attacks, draw_holds, draw_supports
from Functions_Coordinates import get_coordinates, write_coordinates_file

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"
coastal_territory_file = "GUI/Data_Coastal_Names.csv"
coastal_coordinates_file = "GUI/Territory_Coastal_Coordinates.txt"

def get_objects(objects_dictionary, turn):
    commands = objects_dictionary[turn]["Commands"]
    commanders = objects_dictionary[turn]["Commanders"]
    nodes = objects_dictionary[turn]["Nodes"]
    units = objects_dictionary[turn]["Units"]
    nodes = nodes[0]
    assign_coordinates_to_nodes(nodes, coordinates_file, coastal_coordinates_file)
    return commands, commanders, nodes, units

# Create listbox of territories
def create_territory_listbox(main_window, territory_file, scrollbar):
    listbox = tk.Listbox(main_window, yscrollcommand = scrollbar.set)
    opened_file = open(territory_file)
    count = 1
    for entry in opened_file:
        listbox.insert(count, str(entry)[0:3])
        count += 1
    listbox.place(x=700, y=700)
    listbox.pack()
    return listbox

def set_up_gui(game_objects, current_turn, turns):
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    # Close window button
    close_button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    close_button.pack()
    next_turn_button = tk.Button(main_window, text = "Next Turn", width = 20)
    next_turn_button.pack()
    previous_turn_button = tk.Button(main_window, text = "Previous Turn", width = 20)
    previous_turn_button.pack()
    # image
    map_image = Image.open("GUI/kamrans_map_png.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)
    # create canvas to click on 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    return main_window, map_image, canvas, close_button, next_turn_button, previous_turn_button

def display_moves(main_window, map_image, canvas, commands):
    canvas.pack(fill = tk.BOTH)
    # convert pil image to tkinter image object
    map_image = ImageTk.PhotoImage(map_image)
    # create canvas on image
    canvas.create_image(0, 0, anchor = tk.NW, image = map_image)
    """
    # make image label
    map_label = tk.Label(main_window, image = map_image)
    map_label.pack (pady = 10)
    """
    # Display text or images
    display_box = tk.Label(main_window, text = "TGDP Display Box")
    display_box.pack()
    # Scroll bar
    scrollbar = tk.Scrollbar(main_window)
    scrollbar.pack(side = 'right', fill = 'y')
    """
    bind images for clicks to get territory coordinates
    commented out so extra coordinates don't get recorded unintentionally
    """
    #coords = main_window.bind("<Button-1>", get_coordinates)
    listbox = create_territory_listbox(main_window, territory_file, scrollbar)
    scrollbar.config(command = listbox.yview)
    canvas.image = map_image
    canvas = draw_pieces(canvas, commands)
    return main_window

def draw_pieces(canvas, commands):
    canvas = draw_units(canvas, commands)
    canvas = draw_attacks(canvas, commands)
    canvas = draw_holds(canvas, commands)
    canvas = draw_supports(canvas, commands)
    return canvas

def show_next_turn(event, main_window, canvas, game_objects, current_turn, turns, next_turn_button, previous_turn_button):
    if event:
        turns = []
        for turn in game_objects:
            turns.append(turn)
        current_turn_index = turns.index(current_turn)
        next_turn_index = current_turn_index + 1
        next_turn = turns[next_turn_index]
        commands, commanders, nodes, units = get_objects(game_objects, next_turn)
        canvas.delete("draw")
        canvas = draw_pieces(canvas, commands)
        next_turn_button.bind("<Button-1>", lambda event: show_next_turn(event, main_window, canvas, game_objects, next_turn, turns, next_turn_button, previous_turn_button))
        previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(event, main_window, canvas, game_objects, next_turn, turns, previous_turn_button, next_turn_button))

def show_previous_turn(event, main_window, canvas, game_objects, current_turn, turns, previous_turn_button, next_turn_button):
    if event:
        turns = []
        for turn in game_objects:
            turns.append(turn)
        current_turn_index = turns.index(current_turn)
        if current_turn_index != 1:
            previous_turn_index = current_turn_index - 1
        else:
            previous_turn_index = current_turn_index
        previous_turn = turns[previous_turn_index]
        commands, commanders, nodes, units = get_objects(game_objects, previous_turn)
        canvas.delete("draw")
        canvas = draw_pieces(canvas, commands)
        previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(event, main_window, canvas, game_objects, previous_turn, turns, previous_turn_button, next_turn_button))
        next_turn_button.bind("<Button-1>", lambda event: show_next_turn(event, main_window, canvas, game_objects, previous_turn, turns, next_turn_button, previous_turn_button))

def run_gui(game_objects, turn = None):
    turns = []
    for turn in game_objects:
        turns.append(turn)
    first_turn = turns[1]
    commands, commanders, nodes, units = get_objects(game_objects, first_turn)
    main_window, map_image, canvas, close_button, next_turn_button, previous_turn_button = set_up_gui(game_objects, first_turn, turns)
    main_window = display_moves(main_window, map_image, canvas, commands)
    next_turn_button.bind("<Button-1>", lambda event: show_next_turn(main_window, event, canvas, game_objects, first_turn, turns, next_turn_button, previous_turn_button))
    previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(main_window, event, canvas, game_objects, first_turn, turns, previous_turn_button, next_turn_button))
    main_window.mainloop()
