import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
from Functions_Coordinates import assign_coordinates_to_nodes

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"

# retrieve coordinates for territories
def get_coordinates(click):
    if click:
        x_coordinate = click.x
        y_coordinate = click.y
        coordinate = (x_coordinate, y_coordinate)
        coordinates.append(coordinate)
        write_coordinates_file(territory_file, coordinates_file)

# save coordinates for territories in output file
def write_coordinates_file(territory_file, coordinates_file):
    with open(territory_file, "r") as file_input, open(coordinates_file, "a") as file_output:
        count = len(coordinates)
        territory_file_count = 0
        for line in file_input:
            if territory_file_count == count - 1:
                print("current territory is", line)
                print("click the next territory", next(file_input))
                print(line[0:3], coordinates[count - 1], file = file_output)
            territory_file_count += 1

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

# Draw a line on map
def draw_line(map_image): 
    drawing_image = ImageDraw.Draw(map_image)
    coordinates = [(0,0), (200, 200)]
    drawing_image.line(coordinates, fill = "red")

territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"

def assign_coordinates_to_nodes(nodes, coordinate_file):
    for node_id in nodes:
        node = nodes[node_id]
        with open (coordinate_file, "r") as file_input:
            for line in file_input:
                if line[0:3] == node_id:
                    coordinates = line[4:-1]
                    coordinates = tuple(coordinates)
                    node.assign_coordinates(coordinates)
    return nodes

def set_up_gui():
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    # Close window button
    # Button syntax: w = tk.Button (master, option = value)
    button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    button.pack()
    # image
    map_image = Image.open("GUI/kamrans_map_png.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)
    # create canvas to click on 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    canvas.pack(fill = tk.BOTH)
    #draw_line(map_image)
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
    main_window.mainloop()

def run_gui(game_objects):
    """
    for turn in game_objects:
        commands = game_objects[turn]["Commands"]
        commanders = game_objects[turn]["Commanders"]
        nodes = game_objects[turn]["Nodes"]
        units = game_objects[turn]["Units"]
        print(turn)
        #print(turn, commands)
    """
    set_up_gui()
    turn = "8b1908_spring"
    commands = game_objects[turn]["Commands"]
    commanders = game_objects[turn]["Commanders"]
    nodes = game_objects[turn]["Nodes"]
    units = game_objects[turn]["Units"]
    assign_coordinates_to_nodes(nodes, coordinates_file)
    for node_id in nodes:
        print(nodes[node_id].coordinate)
    return game_objects

