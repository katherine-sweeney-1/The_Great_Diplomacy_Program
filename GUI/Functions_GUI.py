"""

# GUI display with buttons for next turn and previous turn
def set_up_gui():
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    close_button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    close_button.pack()
    next_turn_button = tk.Button(main_window, text = "Next Turn", width = 20)
    next_turn_button.pack()
    next_turn_button.place(x = 800, y = 0)
    previous_turn_button = tk.Button(main_window, text = "Previous Turn", width = 20)
    previous_turn_button.pack()
    previous_turn_button.place(x = 0, y = 0)
    map_image = Image.open("GUI/Europe_Map.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS) 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    return main_window, map_image, canvas, next_turn_button, previous_turn_button

# Display the pieces and treeview data
def display_moves(main_window, map_image, canvas, commands, commanders):
    canvas.pack(fill = tk.BOTH)
    map_image = ImageTk.PhotoImage(map_image)
    canvas.create_image(0,0, anchor = tk.NW, image = map_image)
    display_box = tk.Label(main_window, text = "TGDP Display Box")
    display_box.pack()
    scrollbar = tk.Scrollbar(main_window)
    scrollbar.pack(side = 'right', fill = 'y')
    #canvas.image = map_image
    canvas = draw_pieces(canvas, commands)
    treeview = create_treeview(main_window, commanders, commands)
    return main_window, treeview, canvas




# Save the map images with moves as png files
def save_images(game_objects, game_and_turn_string):
    images_directory = "/home/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static"
    main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
    for turn in game_objects:
        commands, commanders, nodes, units = get_objects(game_objects, turn)
        #main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
        main_window, treeview, canvas = display_moves(main_window, map_image, canvas, commands, commanders)
        #canvas.update()
        file_name = "GUI/" + game_and_turn_string + ".png"
        
        #map_width = map_image.width
        #map_height = map_image.height
        #ImageGrab.grab().crop((0,0, map_width, map_height)).save(file_name)
        
        #print("canvas", type(canvas))
        #print("main window", type(main_window))
    


        #main_window.mainloop()
        #canvas.update()
        #canvas.postscript(file = game_and_turn_string, colormode = "color")

        
        #map_width = map_image.width
        #map_height = map_image.height
        #file_name = game_and_turn_string + ".png"

        img = ImageGrab.grab().crop((0, 0, map_width, map_height)).save(file_name)
        img = ImageGrab.grab().crop((0, 0, map_width, map_height))
        file_path = os.path.join(images_directory, game_and_turn_string)
        #img.save(file_path, "PNG")
        canvas = Image.open(canvas)
        #img.save("/home/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static".format(game_and_turn_string), "PNG")
        canvas.save("GUI/{}".format(file_name))
        
"""

import sys
sys.path.append("../The_Great_Diplomacy_Program/Nodes")
from Functions_Node import get_nodes_data_dictionary
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
import ghostscript
from Functions_Drawing import draw_units, draw_attacks, draw_holds, draw_supports
from Functions_Coordinates import get_coordinates, assign_coordinates_to_nodes, get_territories_with_neighbors_coordinates

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coastal_territory_file = "GUI/Data_Coastal_Names.csv"

# coordinates_file = "GUI/Territory_Main_Coordinates.txt"
# coastal_coordinates_file = "GUI/Territory_Coastal_Coordinates.txt"
coordinates_file = "GUI/Europe_Map_Main_Coordinates.txt"
coastal_coordinates_file = "GUI/Europe_Map_Coastal_Coordinates.txt"

# Retrieve objects
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

# Create treeview to display information about each move
def create_treeview(main_window, commanders, commands):
    columns = ("Commander", "Unit ID", "Unit Type", "Action", "Location", "Origin", "Destination")
    treeview = tk.ttk.Treeview(main_window, columns = columns, height = 25, show = "headings")
    treeview = add_treeview_data(treeview, commanders, commands)
    return treeview

# Add the data to the treeview
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

# GUI display with buttons for next turn and previous turn
def set_up_gui():
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    close_button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    close_button.pack()
    next_turn_button = tk.Button(main_window, text = "Next Turn", width = 20)
    next_turn_button.pack()
    next_turn_button.place(x = 800, y = 0)
    previous_turn_button = tk.Button(main_window, text = "Previous Turn", width = 20)
    previous_turn_button.pack()
    previous_turn_button.place(x = 0, y = 0)
    map_image = Image.open("GUI/Europe_Map.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS) 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    return main_window, map_image, canvas, next_turn_button, previous_turn_button

# Display the pieces and treeview data
def display_moves(main_window, map_image, canvas, commands, commanders):
    canvas.pack(fill = tk.BOTH)
    map_image = ImageTk.PhotoImage(map_image)
    canvas.create_image(0,0, anchor = tk.NW, image = map_image)
    display_box = tk.Label(main_window, text = "TGDP Display Box")
    display_box.pack()
    scrollbar = tk.Scrollbar(main_window)
    scrollbar.pack(side = 'right', fill = 'y')
    canvas.image = map_image
    canvas = draw_pieces(canvas, commands)
    treeview = create_treeview(main_window, commanders, commands)
    return main_window, treeview, canvas

# Display a static map with a button feature to retrieve coordinates for nodes
def display_static_map(main_window, map_image, canvas):
    canvas.pack(fill = tk.BOTH)
    map_image = ImageTk.PhotoImage(map_image)
    canvas.create_image(0,0, anchor = tk.NW, image = map_image)
    display_box = tk.Label(main_window, text = "TGDP Display Box")
    display_box.pack()
    scrollbar = tk.Scrollbar(main_window)
    scrollbar.pack(side = 'right', fill = 'y')
    """
    bind images for clicks to get territory coordinates
    commented out so extra coordinates don't get recorded unintentionally
    """
    coords = main_window.bind("<Button-1>", get_coordinates)
    canvas.image = map_image
    return main_window

# Draw the units and movements 
def draw_pieces(canvas, commands):
    canvas = draw_units(canvas, commands)
    canvas = draw_attacks(canvas, commands)
    canvas = draw_holds(canvas, commands)
    canvas = draw_supports(canvas, commands)
    return canvas

# Add treeview data and implement next turn and previous turn buttons
def display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, different_turn, commanders, treeview):
    commands, commanders, nodes, units = get_objects(game_objects, different_turn)
    canvas.delete("draw")
    canvas = draw_pieces(canvas, commands)
    for item in treeview.get_children():
        treeview.delete(item)
    add_treeview_data(treeview, commanders, commands)
    next_turn_button.bind("<Button-1>", lambda event: show_next_turn(event, main_window, canvas, game_objects, different_turn, turns, next_turn_button, previous_turn_button, commanders, treeview))
    previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(event, main_window, canvas, game_objects, different_turn, turns, previous_turn_button, next_turn_button, commanders, treeview))

# Next turn button
def show_next_turn(event, main_window, canvas, game_objects, current_turn, turns, next_turn_button, previous_turn_button, commanders, treeview):
    if event:
        current_turn_index = turns.index(current_turn)
        if current_turn_index != len(turns) - 1:
            next_turn_index = current_turn_index + 1
        else:
            next_turn_index = current_turn_index
        next_turn = turns[next_turn_index]
        display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, next_turn, commanders, treeview)

# Previous turn button
def show_previous_turn(event, main_window, canvas, game_objects, current_turn, turns, previous_turn_button, next_turn_button, commanders, treeview):
    if event:
        current_turn_index = turns.index(current_turn)
        if current_turn_index != 0:
            previous_turn_index = current_turn_index - 1
        else:
            previous_turn_index = current_turn_index
        previous_turn = turns[previous_turn_index]
        display_different_turn(main_window, canvas, game_objects, turns, next_turn_button, previous_turn_button, previous_turn, commanders, treeview)

# Retrieve the coordinates of nodes by clicking on map 
def retrieve_node_coordinates():
    main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
    main_window = display_static_map(main_window, map_image, canvas)
    main_window.mainloop()

# Assign the coordinates to the neighbors of nodes
def assign_neighbor_coordinates():
    data_nodes = "data/Data_Ter_Main.csv"
    data_coastal = "data/Data_Ter_Special_Coasts.csv"
    territory_neighbor_coordinates = "GUI/Europe_Map_Main_and_Neighbors_Coordinates.csv"
    coordinates_file = "GUI/Europe_Map_Main_Coordinates.txt"
    nodes_data_main = get_nodes_data_dictionary(data_nodes)
    get_territories_with_neighbors_coordinates(nodes_data_main, coordinates_file, territory_neighbor_coordinates)

# Save the map images with moves as png files
def save_images(game_objects, game_number_string, start_game_year):
    count = 0
    main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
    for turn in game_objects:
        #print("game year", start_game_year)
        game_year = int(start_game_year)
        game_year = game_year + count/2
        game_year = int(game_year)
        game_season = count % 2
        match game_season:
            case 0:
                game_season = "Spring"
            case 1:
                game_season = "Fall"
        game_season = game_season.lower()
        game_and_turn_string = "game" + str(game_number_string) + "_" + str(game_year) + "_" + game_season
        #print("TURN", turn)
        commands, commanders, nodes, units = get_objects(game_objects, turn)
        #main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
        main_window, treeview, canvas = display_moves(main_window, map_image, canvas, commands, commanders)
        #main_window.mainloop()
        map_width = map_image.width
        map_height = map_image.height
        print(game_and_turn_string)
        print(" ")
        file_name_ps = "GUI/" + game_and_turn_string + ".ps"
        file_name_pdf = game_and_turn_string + ".pdf"
        file_name_png = game_and_turn_string + ".png"
        #print("map width and height map_dimension", map_width, map_height)
        #ImageGrab.grab().crop((0, 0, map_width, map_height)).save(file_name)
        #canvas.delete()
        canvas.update()
        canvas.postscript(file = file_name_ps, colormode = "color")
        """
        img =ImageTk.getimage(canvas.image)
        img.save(file_name_png)
        img.show()
        """
        
        arguments = [
            "postscript_to_pdf",
            "-dNOPAUSE", "-dBATCH", "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-sOutputFile={}".format(file_name_pdf),
            "-f", file_name_ps
        ]
        ghostscript.Ghostscript(*arguments)
        
        count += 1

        #main_window.save(file_name_png)

"""
def save_images(game_objects, game_and_turn_string):
    images_directory = "/home/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static"
    main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
    for turn in game_objects:
        commands, commanders, nodes, units = get_objects(game_objects, turn)
        #main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
        main_window, treeview, canvas = display_moves(main_window, map_image, canvas, commands, commanders)
        #canvas.update()
        file_name = "GUI/" + game_and_turn_string + ".png"
        
        #map_width = map_image.width
        #map_height = map_image.height
        #ImageGrab.grab().crop((0,0, map_width, map_height)).save(file_name)
        
        #print("canvas", type(canvas))
        #print("main window", type(main_window))
    


        #main_window.mainloop()
        #canvas.update()
        #canvas.postscript(file = game_and_turn_string, colormode = "color")

        
        #map_width = map_image.width
        #map_height = map_image.height
        #file_name = game_and_turn_string + ".png"

        img = ImageGrab.grab().crop((0, 0, map_width, map_height)).save(file_name)
        img = ImageGrab.grab().crop((0, 0, map_width, map_height))
        file_path = os.path.join(images_directory, game_and_turn_string)
        #img.save(file_path, "PNG")
        canvas = Image.open(canvas)
        #img.save("/home/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static".format(game_and_turn_string), "PNG")
        canvas.save("GUI/{}".format(file_name))
"""






# Run function
def run_gui(game_objects, game_number_string, start_game_year, save_images_boolean, turn = None):
    
    turns = []
    for turn in game_objects:
        turns.append(turn)
    first_turn = turns[0]
    if save_images_boolean:
        #print("hello")
        save_images(game_objects, game_number_string, start_game_year)
    else:
        commands, commanders, nodes, units = get_objects(game_objects, first_turn)
        main_window, map_image, canvas, next_turn_button, previous_turn_button = set_up_gui()
        main_window, treeview, canvas = display_moves(main_window, map_image, canvas, commands, commanders)
        next_turn_button.bind("<Button-1>", lambda event: show_next_turn(main_window, event, canvas, game_objects, first_turn, turns, next_turn_button, previous_turn_button, commanders, treeview))
        previous_turn_button.bind("<Button-1>", lambda event: show_previous_turn(main_window, event, canvas, game_objects, first_turn, turns, previous_turn_button, next_turn_button, commanders, treeview))
        main_window.mainloop()

"""

add year and season to the map display?

"""