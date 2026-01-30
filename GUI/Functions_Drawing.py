import math
from PIL import Image, ImageTk, ImageDraw

def draw_units(commands, map_image):
    drawing_image = ImageDraw.Draw(map_image)
    for command_id in commands:
        command = commands[command_id]
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
            line_id = drawing_image.ellipse(coordinates, fill, outline = "black", width = 1)
        else:
            south_coordinates = (center[0], center[1] + 5)
            nw_coordinates = (center[0] - 6, center[1] - 6)
            ne_coordinates = (center[0] + 6, center[1] - 6)
            coordinates = [south_coordinates, nw_coordinates, ne_coordinates]
            line_id = drawing_image.polygon(coordinates, fill, outline = "black", width = 1)

def draw_attacks(map_image, commands):
    drawing_image = ImageDraw.Draw(map_image)
    for command_id in commands:
        command = commands[command_id]
    # for attacks
        if command.location == command.origin and command.origin != command.destination:
            first_coordinate = command.origin.coordinate
            second_coordinate = command.destination.coordinate
            second_coordinate = get_offset_destination(first_coordinate, second_coordinate)
            coordinates = [first_coordinate, second_coordinate]
            origin_coordinate = first_coordinate
            destination_coordinate = second_coordinate
            if command.succeed == True:
                fill = "black"
            else:
                fill = "red"
            upper_coordinates, lower_coordinates = get_arrow_coordinates(origin_coordinate, destination_coordinate)
            drawing_image.line(coordinates, fill, width = 2)
            drawing_image.line(upper_coordinates, fill, width = 2)
            drawing_image.line(lower_coordinates, fill, width = 2)  

def draw_holds(map_image, commands):
    drawing_image = ImageDraw.Draw(map_image)
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.origin == command.destination:
            center = command.location.coordinate
            nw_coordinates = (center[0] - 9, center[1] - 9)
            se_coordinates = (center[0] + 9, center[1] + 9)
            coordinates = [nw_coordinates, se_coordinates]
            if command.succeed == True:
                drawing_image.ellipse(coordinates, outline = "black", width = 2)
            else:
                drawing_image.ellipse(coordinates, outline = "red", width = 2)

def get_offset_destination (first_coordinate, second_coordinate):
    if second_coordinate[0] > first_coordinate[0]:
        # destination is bottom right of origin
        if second_coordinate[1] > first_coordinate[1]:
            second_coordinate = (second_coordinate[0] - 6, second_coordinate[1] - 6)
        # destination is top right of origin
        else:
            second_coordinate = (second_coordinate[0] - 6, second_coordinate[1] + 6)
    else:
        # destination is bottom left of origin
        if second_coordinate[1] > first_coordinate[1]:
            second_coordinate = (second_coordinate[0] + 6, second_coordinate[1] - 6)
        # destination is top left of origin
        else:
            second_coordinate = (second_coordinate[0] + 6, second_coordinate[1]+ 6)
    return second_coordinate

def get_arrow_coordinates(origin_coordinate, destination_coordinate):
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
        else:
            slope_upper_line = slope - math.pi/6
            slope_lower_line = slope + math.pi/6
    else:
        if destination_coordinate[1] > origin_coordinate[1]:
            slope_upper_line = slope - math.pi/6
            slope_lower_line = slope + math.pi/6
        else:
            slope_upper_line = slope -  5*math.pi/6
            slope_lower_line = slope + 5*math.pi/6
    upper_x_endpoint = (20*math.cos(slope_upper_line)) + destination_coordinate[0]
    upper_y_endpoint = (20*math.sin(slope_upper_line)) + destination_coordinate[1]
    lower_x_endpoint = (20*math.cos(slope_lower_line)) + destination_coordinate[0]
    lower_y_endpoint = (20*math.sin(slope_lower_line)) + destination_coordinate[1]
    upper_x_endpoint = int(upper_x_endpoint)
    upper_y_endpoint = int(upper_y_endpoint)
    lower_x_endpoint = int(lower_x_endpoint)
    lower_y_endpoint = int(lower_y_endpoint)
    upper_arrow_coordinates = (upper_x_endpoint, upper_y_endpoint)
    upper_coordinates = [upper_arrow_coordinates, destination_coordinate]
    lower_arrow_coordinates = (lower_x_endpoint, lower_y_endpoint)
    lower_coordinates = [lower_arrow_coordinates, destination_coordinate]
    return upper_coordinates, lower_coordinates

def draw_supports(canvas, commands):
    for command_id in commands:
        command = commands[command_id]
        if command.location != command.origin and command.convoy == False:
            if command.succeed == True:
                fill_color = "black"
            else:
                fill_color = "red"
            location_coordinate = command.location.coordinate
            origin_coordinate = command.origin.coordinate
            destination_coordinate = command.destination.coordinate
            offset_destination_coordinate = get_offset_destination(origin_coordinate, destination_coordinate)
            offset_origin_coordinate = get_offset_destination(destination_coordinate, origin_coordinate)
            #offset_destination_coordinate = (destination_coordinate[0] - 5, destination_coordinate[1] - 5)
            canvas.create_line (location_coordinate, origin_coordinate, dash = (5, 2), fill = fill_color, width = 3)
            # supports for attacks
            if command.origin != command.destination:
                upper_coordinates, lower_coordinates = get_arrow_coordinates(offset_origin_coordinate, offset_destination_coordinate)
                canvas.create_line(offset_origin_coordinate, offset_destination_coordinate, dash = (5, 2), fill = fill_color, width = 2, tags = ("draw"))
                canvas.create_line(upper_coordinates, fill = fill_color, width = 2, tags = ("draw"))
                canvas.create_line(lower_coordinates, fill = fill_color, width = 2, tags = ("draw"))
            # supports for holds
            else:
                canvas.create_oval(origin_coordinate[0] - 5, origin_coordinate[1] - 5, origin_coordinate[0] + 5, origin_coordinate[1]+ 5, width = 2, tags = "draw")
    return canvas