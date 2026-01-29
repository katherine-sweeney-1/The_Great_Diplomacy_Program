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

def set_up_gui(commands):
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    # Close window button
    button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    button.pack()
    button = tk.Button(main_window, text = "Next Turn", width = 20)
    button.pack()
    # image
    map_image = Image.open("GUI/kamrans_map_png.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)
    # create canvas to click on 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    return main_window, map_image, canvas

def display_moves(main_window, map_image, canvas, commands):
    draw_units(commands, map_image)
    draw_attacks(map_image, commands)
    draw_holds(map_image, commands)
    canvas.pack(fill = tk.BOTH)
    # convert pil image to tkinter image object
    map_image = ImageTk.PhotoImage(map_image)
    # create canvas on image
    canvas.create_image(0, 0, anchor = tk.NW, image = map_image)

    canvas = draw_supports(canvas, commands)
    #canvas.create_line(50, 100, 350, 100, dash = (5, 2), fill = "blue", width = 3)
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
    #main_window.mainloop()
    return main_window

def show_next_turn(event, main_window, map_image, canvas, game_objects, current_turn):
    if event:
        turn = "81911_fall"
        turns = []
        for turn in game_objects:
            turns.append(turn)
        current_turn_index = turns.index(current_turn)
        print("current turn index", current_turn_index, current_turn)
        next_turn = current_turn_index + 1
        print(next_turn)
        commands = game_objects[next_turn]["Commands"]
        commanders = game_objects[next_turn]["Commanders"]
        nodes = game_objects[next_turn]["Nodes"]
        units = game_objects[next_turn]["Units"]
        nodes = nodes[0]
        main_window = display_moves(main_window, map_image, canvas, commands)
            #print("check", command_id, command.location.name, command.origin.name, command.destination.name)

def run_gui(game_objects, turn = None):
    turns = []
    for turn in game_objects:
        turns.append(turn)
    first_turn = turns[0]
    commands = game_objects[first_turn]["Commands"]
    commanders = game_objects[first_turn]["Commanders"]
    nodes = game_objects[first_turn]["Nodes"]
    units = game_objects[first_turn]["Units"]
    nodes = nodes[0]
    assign_coordinates_to_nodes(nodes, coordinates_file, coastal_coordinates_file)
    for command_id in commands:
        command = commands[command_id]
        #print("check", command_id, command.location.name, command.origin.name, command.destination.name)
    main_window, map_image, canvas = set_up_gui(commands)
    main_window = display_moves(main_window, map_image, canvas, commands)
    main_window.bind("<Button-2>", lambda event: show_next_turn(event, main_window, map_image, canvas, game_objects, first_turn))
    main_window.mainloop()