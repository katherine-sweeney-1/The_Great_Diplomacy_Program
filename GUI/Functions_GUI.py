import tkinter as tk
from tkinter import ttk
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

def create_treeview(main_window, commanders, commands):
    columns = ("Commander", "Unit ID", "Unit Type", "Action", "Location", "Origin", "Destination")
    treeview = tk.ttk.Treeview(main_window, columns = columns, height = 25, show = "headings")
    treeview = add_treeview_data(treeview, commanders, commands)
    return treeview

def add_treeview_data(treeview, commanders, commands):
    columns = ("Commander", "Unit ID", "Unit Type", "Action", "Location", "Origin", "Destination")
    for column_entry in columns:
        treeview.heading(column_entry, text = column_entry)
        treeview.column(column_entry, width = 100)
    for commander_id in commanders:
        commander = commanders[commander_id]
        unit_members = commander.unit_members
        for unit_id in unit_members:
            unit = unit_members[unit_id]
            command = commands[unit_id]
            if command.location == command.origin and command.origin != command.destination:
                action_type = "Attack"
            elif command.location == command.origin and command.origin == command.destination:
                action_type = "Hold"
            elif command.location != command.origin and command.convoy == False:
                action_type = "Support"
            elif command.convoy == True:
                action_type = "Convoy"
            entry_values = (commander_id, unit_id, unit.type, action_type, command.location.name, command.origin.name, command.destination.name)
            treeview.insert("", "end", values = entry_values)
    treeview.pack()
    return treeview

def set_up_gui(game_objects, current_turn, turns):
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    #main_window.configure(background = "white")
    # Close window button
    close_button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    close_button.pack()
    next_turn_button = tk.Button(main_window, text = "Next Turn", width = 20)
    next_turn_button.pack()
    next_turn_button.place(x = 800, y = 0)
    previous_turn_button = tk.Button(main_window, text = "Previous Turn", width = 20)
    previous_turn_button.pack()
    previous_turn_button.place(x = 0, y = 0)
    # image
    map_image = Image.open("GUI/kamrans_map_png.png")
    map_width = map_image.width
    map_height = map_image.height
    
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)
    # create canvas to click on 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    return main_window, map_image, canvas, close_button, next_turn_button, previous_turn_button

def display_moves(main_window, map_image, canvas, commands, commanders):
    canvas.pack(fill = tk.BOTH)
    # convert pil image to tkinter image object
    map_image = ImageTk.PhotoImage(map_image)
    # create canvas on image
    canvas.create_image(0,0, anchor = tk.NW, image = map_image)
    #canvas.create_image(500, 200, anchor = "center", image = map_image)
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
    #listbox = create_territory_listbox(main_window, territory_file, scrollbar)
    #scrollbar.config(command = listbox.yview)
    canvas.image = map_image
    canvas = draw_pieces(canvas, commands)
    treeview = create_treeview(main_window, commanders, commands)
    return main_window, treeview

def draw_pieces(canvas, commands):
    canvas = draw_units(canvas, commands)
    canvas = draw_attacks(canvas, commands)
    canvas = draw_holds(canvas, commands)
    canvas = draw_supports(canvas, commands)
    return canvas

def display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, different_turn, commanders, treeview):
    commands, commanders, nodes, units = get_objects(game_objects, different_turn)
    canvas.delete("draw")
    canvas = draw_pieces(canvas, commands)
    for item in treeview.get_children():
        treeview.delete(item)
    add_treeview_data(treeview, commanders, commands)
    next_turn_button.bind("<Button-1>", lambda event: show_next_turn(event, main_window, canvas, game_objects, different_turn, turns, next_turn_button, previous_turn_button, commanders, treeview))
    previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(event, main_window, canvas, game_objects, different_turn, turns, previous_turn_button, next_turn_button, commanders, treeview))
    #commanders_data_treeview.bind("<Button-1>", lambda event: create_commanders_info_treeview(event: main_window, commanders, commands))

def show_next_turn(event, main_window, canvas, game_objects, current_turn, turns, next_turn_button, previous_turn_button, commanders, treeview):
    if event:
        current_turn_index = turns.index(current_turn)
        if current_turn_index != len(turns) - 1:
            next_turn_index = current_turn_index + 1
        else:
            next_turn_index = current_turn_index
        next_turn = turns[next_turn_index]
        display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, next_turn, commanders, treeview)

def show_previous_turn(event, main_window, canvas, game_objects, current_turn, turns, previous_turn_button, next_turn_button, commanders, treeview):
    if event:
        current_turn_index = turns.index(current_turn)
        if current_turn_index != 1:
            previous_turn_index = current_turn_index - 1
        else:
            previous_turn_index = current_turn_index
        previous_turn = turns[previous_turn_index]
        display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, previous_turn, commanders, treeview)

def run_gui(game_objects, turn = None):
    turns = []
    for turn in game_objects:
        turns.append(turn)
    first_turn = turns[0]
    commands, commanders, nodes, units = get_objects(game_objects, first_turn)
    main_window, map_image, canvas, close_button, next_turn_button, previous_turn_button = set_up_gui(game_objects, first_turn, turns)
    main_window, treeview = display_moves(main_window, map_image, canvas, commands, commanders)
    #create_commanders_info_treeview(main_window, commanders, commands)
    next_turn_button.bind("<Button-1>", lambda event: show_next_turn(main_window, event, canvas, game_objects, first_turn, turns, next_turn_button, previous_turn_button, commanders, treeview))
    previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(main_window, event, canvas, game_objects, first_turn, turns, previous_turn_button, next_turn_button, commanders, treeview))
    main_window.mainloop()
