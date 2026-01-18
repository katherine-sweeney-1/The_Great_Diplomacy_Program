import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
from Functions_Coordinates import assign_coordinates_to_nodes
import math
import numpy as np
from scipy.optimize import curve_fit

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

def draw_units_test(commands, map_image):
    drawing_image = ImageDraw.Draw(map_image)
    units_coordinates = []
    for command_id in commands:
        command = commands[command_id]
        #print("checking", unit.location.name)
        center = command.location.coordinate
        if command_id[0:2] == "AU":
            fill = (200, 50, 50)
        elif command_id[0:2] == "UK":
            fill = (255, 50, 150)
        elif command_id[0:2] == "FR":
            fill = (0, 75, 100)
        elif command_id[0:2] == "GE":
            fill = (100, 50, 25)
        elif command_id[0:2] == "IT":
            fill = (75, 100, 0)
        elif command_id[0:2] == "RU":
            fill = (75, 25, 75)
        elif command_id[0:2] == "TU":
            fill = (250, 225, 20)
        if command.unit.type == "army":
            nw_coordinates = (center[0] - 5, center[1] - 5)
            se_coordinates = (center[0] + 5, center[1] + 5)
            coordinates = [nw_coordinates, se_coordinates]
            drawing_image.ellipse(coordinates, fill, outline = "black", width = 1)
        elif command.unit.type == "fleet":
            south_coordinates = (center[0], center[1] + 5)
            nw_coordinates = (center[0] - 6, center[1] - 6)
            ne_coordinates = (center[0] + 6, center[1] - 6)
            coordinates = [south_coordinates, nw_coordinates, ne_coordinates]
            drawing_image.polygon(coordinates, fill, outline = "black", width = 1)

def draw_moves(map_image, commands):
    drawing_image = ImageDraw.Draw(map_image)
    for command_id in commands:
        command = commands[command_id]
    # for attacks
        if command.location == command.origin and command.origin != command.destination:
            first_coordinate = command.origin.coordinate
            second_coordinate = command.destination.coordinate
            draw_line_from_coordinates(first_coordinate, second_coordinate, command, drawing_image)
            """
            coordinates = [command.origin.coordinate, command.destination.coordinate]
            origin_coordinate = command.origin.coordinate
            destination_coordinate = command.destination.coordinate
            slope = (destination_coordinate[1] - origin_coordinate[1])/(destination_coordinate[0] - origin_coordinate[0])
            if slope > 0:
                sign = True
            else:
                sign = False
            slope = round(slope, 2)
            slope = math.atan(slope)
            slope = round(slope, 2)
            if sign == True:
                if command.destination.coordinate[1] > command.origin.coordinate[1]:
                    slope_upper_line = slope - 5*math.pi/6
                    slope_lower_line = slope + 5*math.pi/6
                    upper_x_endpoint = 20*math.cos(slope_upper_line) + destination_coordinate[0]
                    upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
                    lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
                    lower_y_endpoint = 20*math.sin(slope_lower_line) + destination_coordinate[1]
                else:
                    slope_upper_line = slope - math.pi/6
                    slope_lower_line = slope + math.pi/6
                    upper_x_endpoint = 20*math.cos(slope_upper_line) + destination_coordinate[0]
                    upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
                    lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
                    lower_y_endpoint = 20*math.sin(slope_lower_line) + destination_coordinate[1]
            else:
                if command.destination.coordinate[1] > command.origin.coordinate[1]:
                    #print("yes", command_id, command.location.name)
                    slope_upper_line = slope + 11*math.pi/6
                    slope_lower_line = slope + math.pi/6
                    upper_x_endpoint = (20*math.cos(slope_upper_line)) + destination_coordinate[0]
                    upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
                    lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
                    lower_y_endpoint = (20*math.sin(slope_lower_line)) + destination_coordinate[1]
                else:
                    slope_upper_line = slope -  5*math.pi/6
                    slope_lower_line = slope + 5*math.pi/6
                    upper_x_endpoint = (20*math.cos(slope_upper_line)) + destination_coordinate[0]
                    upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
                    lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
                    lower_y_endpoint = (20*math.sin(slope_lower_line)) + destination_coordinate[1]
            upper_x_endpoint = int(upper_x_endpoint)
            upper_y_endpoint = int(upper_y_endpoint)
            upper_arrow_coordinates = (upper_x_endpoint, upper_y_endpoint)
            upper_coordinates = [upper_arrow_coordinates, destination_coordinate]
            lower_x_endpoint = int(lower_x_endpoint)
            lower_y_endpoint = int(lower_y_endpoint)
            lower_arrow_coordinates = (lower_x_endpoint, lower_y_endpoint)
            lower_coordinates = [lower_arrow_coordinates, destination_coordinate]
            if command.succeed == True:
                fill = "black"
            else:
                fill = "red"
            drawing_image.line(coordinates, fill, width = 2)
            drawing_image.line(upper_coordinates, fill, width = 2)
            drawing_image.line(lower_coordinates, fill, width = 2)
            """
    # for supports
        if command.location != command.origin and command.convoy == False:
            points = []
            """
            if command.destination.coordinate[1] > command.location.coordinate[1]:
                y_larger_value = command.destination.coordinate[1]
            else:
                y_larger_value = command.location.coordinate[1]
            """
            if command.destination.coordinate[0] > command.location.coordinate[0]:
                x_start_point = command.location.coordinate[0]
                y_start_point = command.location.coordinate[1]
                x_end_point = command.destination.coordinate[0]
                y_end_point = command.destination.coordinate[1]
                #a = x_start_point*(x_start_point - x_end_point)
            else:
                x_start_point = command.destination.coordinate[0]
                y_start_point = command.destination.coordinate[1]
                x_end_point = command.location.coordinate[0]
                y_end_point = command.location.coordinate[1]
                a = x_end_point*(x_end_point - x_start_point)
            if command.destination.coordinate[1] > command.location.coordinate[1]:
                x_vertex = 2*(x_end_point - x_start_point)/3 + x_start_point
            else:
                x_vertex = (x_end_point - x_start_point)/3 + x_start_point
            x_values = np.arange(x_start_point, x_end_point, 1)
            #x_vertex = (x_end_point - x_start_point)/2 + x_start_point
            #y_vertex = y_larger_value + 15
            #vertex = (x_vertex, y_vertex)
            x_origin = command.origin.coordinate[0]
            y_origin = command.origin.coordinate[1]
            #b = x_start_point*(y_start_point - y_end_point) - y_start_point
            initial_x_values = [command.location.coordinate[0], command.destination.coordinate[0]]
            initial_y_values = [command.location.coordinate[1], (command.origin.coordinate[0] - 5), (command.destination.coordinate[0] - 1), command.destination.coordinate[1]]
            initial_parameter_values = [1.0, 1.0, 0.0, 0.0]
            #parameters = curve_fit(tangent_function, xdata = initial_x_values, ydata = initial_y_values)
            #b = parameters
            print("initial", initial_x_values)
            minimum_x = min(initial_x_values)
            maximum_x = max(initial_x_values)
            print(minimum_x, maximum_x)
            x_values = np.linspace(minimum_x, maximum_x)
            points = []
            print(x_values)
            for x in x_values:
                b = 1
                y = tangent_function(x, x_origin, y_origin)
                print("x", x)
                print("y", y)
                points.append((x, y))
            """
            for x in x_values:
                #x = np.cosh(x)
                #y = np.sinh(x)
                print(x, a)
                print(x**2/a**2)
                if x == 0 :
                    continue
                else:
                    y_positive = b*math.sqrt((x**2)/(a**2) - 1)
                    print(y_positive)
                    points.append((x, y_positive))
            """
            outline = "green"
            drawing_image.line(points, outline, width = 3)    
            """
            #x = np.linspace(x_start_point, x_end_point, number_of_points)
            a = (y_start_point - vertex[1])/(x_start_point - vertex[0])**2
            y_values = a*(x_values - vertex[0])**2 + vertex[1]
            for x, y in zip(x_values, y_values):
                # destination coordinate is below location coordinate on the map
                if command.destination.coordinate[1] > command.location.coordinate[1]:
                    if x > x_start_point and x < vertex[0] and y > y_start_point:
                        x = int(x)
                        y = int(y)
                        points.append((x, y)) 
                        outline = "black"
                    if x > vertex[0] and x < x_end_point and y > y_end_point:
                        x = int(x)
                        y = int(y)
                        points.append((x, y)) 
                        outline = "red"
                else:
                    # may need to revise this code
                    if x > x_start_point and x < vertex[0] and y > y_start_point:
                        #print("yes 1", command_id)
                        x = int(x)
                        y = int(y)
                        points.append((x, y))
                        outline = "blue"
                    #print("ues", command_id, int(x), x_end_point)
                    #print("yes 2", command_id, int(y), y_end_point)
                    if x > vertex[0] and x < x_end_point and y > y_end_point:
                        print("yes 2", command_id, command.destination.name, "x", x, "y", int(y), y_end_point)
                        print(command.location.name, command.destination.name, command.location.coordinate, command.destination.coordinate)
                        print(" ")
                        x = int(x)
                        y = int(y)
                        points.append((x, y))
                        outline = "green"

                    #outline = "black"     
            drawing_image.line(points, outline, width = 3)
            """
    #for holds
        if command.location == command.origin == command.destination:
            center = command.location.coordinate
            nw_coordinates = (center[0] - 9, center[1] - 9)
            se_coordinates = (center[0] + 9, center[1] + 9)
            coordinates = [nw_coordinates, se_coordinates]
            if command.succeed == True:
                drawing_image.ellipse(coordinates, outline = "black", width = 2)
            else:
                drawing_image.ellipse(coordinates, outline = "red", width = 2)
    # for convoys

def tangent_function(x, x_origin, y_origin):
    y = 10*np.tanh((10*x+ x_origin)) + y_origin
    return y

# Draw a line on map
def draw_line_from_coordinates(first_coordinate, second_coordinate, command, drawing_image):
    coordinates = [first_coordinate, second_coordinate]
    origin_coordinate = first_coordinate
    destination_coordinate = second_coordinate
    slope = (destination_coordinate[1] - origin_coordinate[1])/(destination_coordinate[0] - origin_coordinate[0])
    if slope > 0:
        sign = True
    else:
        sign = False
    slope = round(slope, 2)
    slope = math.atan(slope)
    slope = round(slope, 2)
    if sign == True:
        if destination_coordinate[1] > origin_coordinate[1]:
            slope_upper_line = slope - 5*math.pi/6
            slope_lower_line = slope + 5*math.pi/6
            upper_x_endpoint = 20*math.cos(slope_upper_line) + destination_coordinate[0]
            upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
            lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
            lower_y_endpoint = 20*math.sin(slope_lower_line) + destination_coordinate[1]
        else:
            slope_upper_line = slope - math.pi/6
            slope_lower_line = slope + math.pi/6
            upper_x_endpoint = 20*math.cos(slope_upper_line) + destination_coordinate[0]
            upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
            lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
            lower_y_endpoint = 20*math.sin(slope_lower_line) + destination_coordinate[1]
    else:
        if destination_coordinate[1] > origin_coordinate[1]:
            #print("yes", command_id, command.location.name)
            slope_upper_line = slope + 11*math.pi/6
            slope_lower_line = slope + math.pi/6
            upper_x_endpoint = (20*math.cos(slope_upper_line)) + destination_coordinate[0]
            upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
            lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
            lower_y_endpoint = (20*math.sin(slope_lower_line)) + destination_coordinate[1]
        else:
            slope_upper_line = slope -  5*math.pi/6
            slope_lower_line = slope + 5*math.pi/6
            upper_x_endpoint = (20*math.cos(slope_upper_line)) + destination_coordinate[0]
            upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
            lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
            lower_y_endpoint = (20*math.sin(slope_lower_line)) + destination_coordinate[1]
    upper_x_endpoint = int(upper_x_endpoint)
    upper_y_endpoint = int(upper_y_endpoint)
    upper_arrow_coordinates = (upper_x_endpoint, upper_y_endpoint)
    upper_coordinates = [upper_arrow_coordinates, destination_coordinate]
    lower_x_endpoint = int(lower_x_endpoint)
    lower_y_endpoint = int(lower_y_endpoint)
    lower_arrow_coordinates = (lower_x_endpoint, lower_y_endpoint)
    lower_coordinates = [lower_arrow_coordinates, destination_coordinate]
    if command.succeed == True:
        fill = "black"
    else:
        fill = "red"
    drawing_image.line(coordinates, fill, width = 2)
    drawing_image.line(upper_coordinates, fill, width = 2)
    drawing_image.line(lower_coordinates, fill, width = 2)

def set_up_gui(commands):
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
    draw_units_test(commands, map_image)
    draw_moves(map_image, commands)
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
    turn = "81911_spring"
    commands = game_objects[turn]["Commands"]
    commanders = game_objects[turn]["Commanders"]
    nodes = game_objects[turn]["Nodes"]
    units = game_objects[turn]["Units"]
    nodes = nodes[0]
    assign_coordinates_to_nodes(nodes, coordinates_file, coastal_coordinates_file)
    for command_id in commands:
        command = commands[command_id]
        print("check", command_id, command.location.name, command.origin.name, command.destination.name)
    set_up_gui(commands)
    return game_objects

