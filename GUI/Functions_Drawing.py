import math

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
    elif slope < 0:
        sign = False
    else:
        sign = "zero slope"
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
    elif sign == False:
        if destination_coordinate[1] > origin_coordinate[1]:
            slope_upper_line = slope - math.pi/6
            slope_lower_line = slope + math.pi/6
        else:
            slope_upper_line = slope -  5*math.pi/6
            slope_lower_line = slope + 5*math.pi/6
    elif sign == "zero slope":
        if destination_coordinate[0] > origin_coordinate[0]:
            slope_upper_line = slope - 5*math.pi/6
            slope_lower_line = slope + 5*math.pi/6
        else:
            slope_upper_line = slope - math.pi/6
            slope_lower_line = slope + math.pi/6
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
    return upper_coordinates, lower_coordinates, fill_color

def retrieve_hex_color(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def draw_units(canvas, commands):
    for command_id in commands:
        command = commands[command_id]
        center = command.location.coordinate
        if command_id[0:2] == "AU":
            fill_color = (200, 50, 50)
            fill_color = retrieve_hex_color(200, 50, 50)
        elif command_id[0:2] == "UK":
            fill_color = (255, 50, 150)
            fill_color = retrieve_hex_color(255, 50, 150)
        elif command_id[0:2] == "FR":
            fill_color = (0, 75, 100)
            fill_color = retrieve_hex_color(0, 75, 100)
        elif command_id[0:2] == "GE":
            fill_color = (100, 50, 25)
            fill_color = retrieve_hex_color(100, 50, 25)
        elif command_id[0:2] == "IT":
            fill_color = (75, 100, 0)
            fill_color = retrieve_hex_color(75, 100, 0)
        elif command_id[0:2] == "RU":
            fill_color = (75, 25, 75)
            fill_color = retrieve_hex_color(75, 25, 75)
        elif command_id[0:2] == "TU":
            fill_color = (250, 225, 20)
            fill_color = retrieve_hex_color(250, 225, 20)
        if command.unit.type == "army":
            nw_coordinates = (center[0] - 5, center[1] - 5)
            se_coordinates = (center[0] + 5, center[1] + 5)
            coordinates = [nw_coordinates, se_coordinates]
            canvas.create_oval(coordinates, fill = fill_color, outline = "black", width = 1, tags = ("draw"))
        else:
            south_coordinates = (center[0], center[1] + 5)
            nw_coordinates = (center[0] - 6, center[1] - 6)
            ne_coordinates = (center[0] + 6, center[1] - 6)
            coordinates = [south_coordinates, nw_coordinates, ne_coordinates]
            canvas.create_polygon(coordinates, fill = fill_color, outline = "black", width = 1, tags = ("draw"))
    return canvas 

def draw_attacks(canvas, commands):
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
                fill_color = "black"
            else:
                fill_color = "red"
            upper_coordinates, lower_coordinates, fill_color = get_arrow_coordinates(origin_coordinate, destination_coordinate)
            canvas.create_line(coordinates, fill = fill_color, width = 2, tags = ("draw"))
            canvas.create_line(upper_coordinates, fill = fill_color, width = 2, tags = ("draw"))
            canvas.create_line(lower_coordinates, fill = fill_color, width = 2, tags = ("draw"))  
    return canvas

def draw_holds(canvas, commands):
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.origin == command.destination:
            center = command.location.coordinate
            nw_coordinates = (center[0] - 9, center[1] - 9)
            se_coordinates = (center[0] + 9, center[1] + 9)
            coordinates = [nw_coordinates, se_coordinates]
            if command.succeed == True:
                canvas.create_oval(coordinates, outline = "black", width = 2, tags = ("draw"))
            else:
                canvas.create_oval(coordinates, outline = "red", width = 2, tags = ("draw"))
    return canvas

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
            canvas.create_line (location_coordinate, origin_coordinate, dash = (5, 2), fill = fill_color, width = 3, tags = ("draw"))
            # supports for attacks
            if command.origin != command.destination:
                upper_coordinates, lower_coordinates, fill_color = get_arrow_coordinates(offset_origin_coordinate, offset_destination_coordinate)
                canvas.create_line(offset_origin_coordinate, offset_destination_coordinate, dash = (5, 2), fill = fill_color, width = 2, tags = ("draw"))
                canvas.create_line(upper_coordinates, fill = fill_color, width = 2, tags = ("draw"))
                canvas.create_line(lower_coordinates, fill = fill_color, width = 2, tags = ("draw"))
            # supports for holds
            else:
                canvas.create_oval(origin_coordinate[0] - 5, origin_coordinate[1] - 5, origin_coordinate[0] + 5, origin_coordinate[1]+ 5, width = 2, tags = ("draw"))
    return canvas