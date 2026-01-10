import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
from Functions_Coordinates import assign_coordinates_to_nodes

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coordinates_file = "GUI/Territory_Main_Coordinates.txt"
coastal_territory_file = "GUI/Data_Coastal_Names.csv"
coastal_coordinates_file = "GUI/Territory_Coastal_Coordinates.txt"

# retrieve coordinates for territories
def get_coordinates(click):
    if click:
        x_coordinate = click.x
        y_coordinate = click.y
        coordinate = (x_coordinate, y_coordinate)
        coordinates.append(coordinate)
        write_coordinates_file(coastal_territory_file, coastal_coordinates_file)

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

def draw_units_test(units, map_image):
    drawing_image = ImageDraw.Draw(map_image)
    units_coordinates = []
    for unit_id in units:
        unit = units[unit_id]
        center = unit.location.coordinate
        #print(unit_id, unit.location.name, unit.location.coordinate)
        nw_coordinates = (center[0] - 5, center[1] - 5)
        se_coordinates = (center[0] + 5, center[1] + 5)
        coordinates = [nw_coordinates, se_coordinates]
        units_coordinates.append(coordinates)
        fill = "red"
    for coordinate in units_coordinates:
        #print(coordinate)
        drawing_image.ellipse(coordinate, fill)
"""
def draw_units_on_map(units, map_image, canvas, last_unit_value= None, drawn_units = None, drawn_map_image = None):
    if last_unit_value == None:
        for unit_id in units:
            last_unit = unit_id
    else:
        last_unit = last_unit_value
    if drawn_units == None:
        already_drawn_units = []
    else:
        already_drawn_units = drawn_units
    for unit_id in units:
        unit = units[unit_id]
        #print(unit_id)
        #print("checkin", unit_id, drawn_map_image)
        if unit_id in already_drawn_units:
            continue
        else:
            #print("yes 0")
            already_drawn_units.append(unit_id)
            #print(len(already_drawn_units))
            if unit_id != last_unit and unit not in already_drawn_units:
                #print("yes 1")
                map_image_with_previous_units = drawn_map_image
                #print("len already drawn units", unit_id, len(already_drawn_units))
                if len(already_drawn_units) == 1:
                    print("check", unit_id)
                    map_image_with_unit = draw_unit(unit, map_image, canvas)
                else:
                    print("test ", unit_id)
                    map_image_with_unit = draw_unit(unit, map_image, canvas, map_image_with_previous_units)
                print(map_image_with_unit)
                map_image_with_unit = draw_units_on_map(units, map_image, canvas, last_unit_value = last_unit, drawn_units = already_drawn_units, drawn_map_image = map_image_with_unit)
            elif unit_id == last_unit:
                print("yes 2")
                map_image_with_previous_units = drawn_map_image
                map_image_with_units = draw_unit(unit, map_image, canvas, map_image_with_previous_units)
                return map_image_with_units
    #return map_image
"""
# Draw a line on map
def draw_line(map_image): 
    coordinates = [[(0,0), (200, 200)],[(100, 150), 200, 250]]
    drawing_image = ImageDraw.Draw(map_image)
    for coordinate in coordinates:
        drawing_image.line(coordinate, fill = "red")

def set_up_gui(units):
    main_window = tk.Tk()
    main_window.title('TGDP GUI')
    main_window.geometry("1000x1000")
    # Close window button
    button = tk.Button(main_window, text = "Close", width = 25, command = main_window.destroy)
    button.pack()
    # image
    map_image = Image.open("GUI/kamrans_map_png.png")
    map_width = map_image.width
    map_height = map_image.height
    map_image.thumbnail((map_width, map_height), Image.Resampling.LANCZOS)
    # create canvas to click on 
    canvas = tk.Canvas(main_window, width = map_width, height = map_height, cursor = "cross")
    #draw_line(map_image)
    draw_units_test(units, map_image)
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
    main_window.mainloop()

def run_gui(game_objects):
    turn = "81908_spring"
    commands = game_objects[turn]["Commands"]
    commanders = game_objects[turn]["Commanders"]
    nodes = game_objects[turn]["Nodes"]
    units = game_objects[turn]["Units"]
    nodes = nodes[0]
    assign_coordinates_to_nodes(nodes, coordinates_file, coastal_coordinates_file)
    for unit_id in units:
        print(unit_id, units[unit_id].location.name, units[unit_id].location.coordinate)
    set_up_gui(units)
    return game_objects

