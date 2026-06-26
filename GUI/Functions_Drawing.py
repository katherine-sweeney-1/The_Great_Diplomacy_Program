import math

# Fill color of arrows
def get_fill_color(command):
    if command.succeed == True:
        if command.location == command.origin and command.origin != command.destination:
            fill_color = "green"
        else:
            fill_color = "blue"
    else:
        if command.original_support_origin != False:
            fill_color = "orange"
        else:
            fill_color = "red"
    return fill_color

# Offset arrows so they don't begin and end exactly where the units are 
def get_offset_destination (first_coordinate, second_coordinate, integer):
    if second_coordinate[0] > first_coordinate[0]:
        # destination is bottom right of origin
        if second_coordinate[1] > first_coordinate[1]:
            second_coordinate = (second_coordinate[0] - integer, second_coordinate[1] - integer)
        # destination is top right of origin
        else:
            second_coordinate = (second_coordinate[0] - integer, second_coordinate[1] + integer)
    else:
        # destination is bottom left of origin
        if second_coordinate[1] > first_coordinate[1]:
            second_coordinate = (second_coordinate[0] + integer, second_coordinate[1] - integer)
        # destination is top left of origin
        else:
            second_coordinate = (second_coordinate[0] + integer, second_coordinate[1]+ integer)
    return second_coordinate

# Retrieve coordinates of arrows 
def get_arrow_coordinates(origin_coordinate, destination_coordinate):
    if destination_coordinate[0] - origin_coordinate[0] == 0:
        destination_x_value = destination_coordinate[0] + 1
        destination_y_value = destination_coordinate[1]
        destination_coordinate = (destination_x_value, destination_y_value)
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
    upper_x_endpoint = (15*math.cos(slope_upper_line)) + destination_coordinate[0]
    upper_y_endpoint = (15*math.sin(slope_upper_line)) + destination_coordinate[1]
    lower_x_endpoint = (15*math.cos(slope_lower_line)) + destination_coordinate[0]
    lower_y_endpoint = (15*math.sin(slope_lower_line)) + destination_coordinate[1]
    upper_x_endpoint = int(upper_x_endpoint)
    upper_y_endpoint = int(upper_y_endpoint)
    lower_x_endpoint = int(lower_x_endpoint)
    lower_y_endpoint = int(lower_y_endpoint)
    upper_arrow_coordinates = (upper_x_endpoint, upper_y_endpoint)
    upper_coordinates = [upper_arrow_coordinates, destination_coordinate]
    lower_arrow_coordinates = (lower_x_endpoint, lower_y_endpoint)
    lower_coordinates = [lower_arrow_coordinates, destination_coordinate]
    return upper_coordinates, lower_coordinates

# Hex color
def retrieve_hex_color(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Draw units on map
def draw_units(canvas, commands, winter_boolean):
    for command_id in commands:
        command = commands[command_id]
        if winter_boolean == True:
            if command.winter_location != False:
                center = command.winter_location.coordinate
            else:
                continue
        else:
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

"""

might need to do original location 

"""
# Draw attack arrows 
def draw_attacks(canvas, commands, line_width):
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.origin and command.origin != command.destination:
            first_coordinate = command.origin.coordinate
            second_coordinate = command.destination.coordinate
            second_coordinate = get_offset_destination(first_coordinate, second_coordinate, 2)
            coordinates = [first_coordinate, second_coordinate]
            origin_coordinate = first_coordinate
            destination_coordinate = second_coordinate
            upper_coordinates, lower_coordinates= get_arrow_coordinates(origin_coordinate, destination_coordinate)
            fill_color = get_fill_color(command)
            canvas.create_line(coordinates, fill = fill_color, width = line_width, tags = ("draw"))
            canvas.create_line(upper_coordinates, fill = fill_color, width = line_width, tags = ("draw"))
            canvas.create_line(lower_coordinates, fill = fill_color, width =  line_width, tags = ("draw"))  
    return canvas

# Draw hold circles
def draw_holds(canvas, commands, line_width):
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.origin == command.destination:
            center = command.location.coordinate
            nw_coordinates = (center[0] - 9, center[1] - 9)
            se_coordinates = (center[0] + 9, center[1] + 9)
            coordinates = [nw_coordinates, se_coordinates]
            fill_color = get_fill_color(command)
            canvas.create_oval(coordinates, outline = fill_color, width = line_width, tags = ("draw"))
    return canvas

"""

might need to use original support origin and original support destination and original location

"""
# Draw support dashed lines
def draw_supports(canvas, commands, line_width):
    for command_id in commands:
        command = commands[command_id]
        if command.location != command.origin: 
            location_coordinate = command.location.coordinate
            origin_coordinate = command.origin.coordinate
            destination_coordinate = command.destination.coordinate
            offset_destination_coordinate = get_offset_destination(origin_coordinate, destination_coordinate, 8)
            offset_origin_coordinate = get_offset_destination(destination_coordinate, origin_coordinate, 5)
            fill_color = get_fill_color(command)
            canvas.create_line (location_coordinate, origin_coordinate, dash = (5, 2), fill = fill_color, width = line_width, tags = ("draw"))
            # supports for attacks
            if command.origin != command.destination:
                upper_coordinates, lower_coordinates = get_arrow_coordinates(offset_origin_coordinate, offset_destination_coordinate)
                canvas.create_line(offset_origin_coordinate, offset_destination_coordinate, dash = (5, 2), fill = fill_color, width = 1, tags = ("draw"))
                canvas.create_line(upper_coordinates, fill = fill_color, width = line_width, tags = ("draw"))
                canvas.create_line(lower_coordinates, fill = fill_color, width = line_width, tags = ("draw"))
            # supports for holds
            else:
                canvas.create_oval(origin_coordinate[0] - 5, origin_coordinate[1] - 5, origin_coordinate[0] + 5, origin_coordinate[1]+ 5, width = line_width, tags = ("draw"))
    return canvas

def draw_retreats(canvas, commands, line_width, units):
    for command_id in commands:
        command = commands[command_id]
        if command.succeed == False and command.retreat == True and command_id in units.keys():
            location_coordinate = command.location.coordinate
            retreat_coordinate = units[command_id].location.coordinate
            offset_retreat_coordinate = get_offset_destination(location_coordinate, retreat_coordinate, 2)
            coordinates = [location_coordinate, offset_retreat_coordinate]
            upper_coordinates, lower_coordinates = get_arrow_coordinates (location_coordinate, offset_retreat_coordinate)
            canvas.create_line(coordinates, fill = "yellow", width = line_width, tags = ("draw"))
            canvas.create_line(upper_coordinates, fill = "yellow", width = line_width, tags = ("draw"))
            canvas.create_line(lower_coordinates, fill = "yellow", width =  line_width, tags = ("draw"))
    return canvas


def draw_disbands(canvas, commands, line_width, units):
    disband_line_length = 10
    for command_id in commands:
        command = commands[command_id]
        if command.succeed == False and command_id not in units.keys():
            northwest_coordinate = [command.location.coordinate[0] - disband_line_length, command.location.coordinate[1] + disband_line_length]
            southwest_coordinate = [command.location.coordinate[0] - disband_line_length, command.location.coordinate[1] - disband_line_length]
            northeast_coordinate = [command.location.coordinate[0] + disband_line_length, command.location.coordinate[1] + disband_line_length]
            southeast_coordinate = [command.location.coordinate[0] + disband_line_length, command.location.coordinate[1] - disband_line_length]
            line_1_coordinates = [southwest_coordinate, northeast_coordinate]
            line_2_coordinates = [southeast_coordinate, northwest_coordinate]
            canvas.create_line(line_1_coordinates, fill = "yellow", width = line_width, tags = ("draw"))
            canvas.create_line(line_2_coordinates, fill = "yellow", width = line_width, tags = ("draw"))
    return canvas

# Draw the units and movements 
def draw_map_components(canvas, commands, current_turn_index, line_width, units, displayed_last_turn, last_turn = None):
    if current_turn_index % 3 == 2:
        winter_boolean = True
    else:
        winter_boolean = False
    for command_id in commands:
        command = commands[command_id]
        if command.original_support_origin != False and command.original_support_destination != False:
            command.origin = command.original_support_origin
            command.destination = command.original_support_destination
        if command.original_coastal_location != False:
            command.location = command.original_coastal_location
    canvas = draw_units(canvas, commands, winter_boolean)
    """
    if winter_boolean == False and displayed_last_turn == False:
        #if last_turn == False:
        canvas = draw_attacks(canvas, commands, line_width)
        canvas = draw_holds(canvas, commands, line_width)
        canvas = draw_supports(canvas, commands, line_width)
        canvas = draw_retreats(canvas, commands, line_width, units)
        canvas = draw_disbands(canvas, commands, line_width, units)
    """
    if winter_boolean == False:# and displayed_last_turn == False:
        canvas = draw_attacks(canvas, commands, line_width)
        canvas = draw_holds(canvas, commands, line_width)
        canvas = draw_supports(canvas, commands, line_width)
        canvas = draw_retreats(canvas, commands, line_width, units)
        canvas = draw_disbands(canvas, commands, line_width, units)
        
    if last_turn:
        #displayed_last_turn = True
        """
        # enable the previous turn button to show arrows for the N - 1 turn
        if displayed_last_turn == True:
            displayed_last_turn = False
        else:
            displayed_last_turn = True
        """
    else:
        displayed_last_turn = False
    return canvas, displayed_last_turn

"""
probably fix last turn issue probably in line 238

"""

"""
currently need to display latest turn for submission 
"""