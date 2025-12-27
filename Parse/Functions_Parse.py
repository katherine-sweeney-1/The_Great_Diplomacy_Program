def determine_node_name(line, loc_count, origin_count, dest_count):       
    stripped_line = line[2:]
    location = stripped_line[loc_count : loc_count + 3]
    convoy_boolean = False
    # get location
    if loc_count != 0:
        location = stripped_line[0:6]
    else:
        location = stripped_line[0:3]
    # supports --> get origin and destination
    if stripped_line[loc_count + 3 : loc_count + 6] == " S ":
        # supports --> get origin
        origin = stripped_line[loc_count + 6 : loc_count + origin_count + 9]
        # supports --> get destination for supporting attacks
        if "to" in stripped_line:
            destination = stripped_line[loc_count + origin_count + 13: loc_count + origin_count + dest_count+ 16]
        # supports --> get destination for supporting holds
        else:
            destination = origin
    # convoys --> get origin and destination
    elif stripped_line[loc_count + 3 : loc_count + 6] == " C ":
        convoy_boolean = True
        origin = stripped_line[loc_count + 6: loc_count + origin_count + 9]
        destination = stripped_line[loc_count + origin_count + 13 : loc_count + origin_count + dest_count + 16]
    # holds --> get origin and destination
    elif stripped_line[loc_count + 4] == "H":
        origin = location
        destination = location
    # attacks --> get origin and destination
    else:
        if stripped_line[7:9] == "to":
            origin = stripped_line[0 : loc_count + 3]
        else:
            origin = stripped_line[loc_count + 0 : loc_count+ 3]
        destination = stripped_line[loc_count + origin_count + 7 : loc_count + origin_count + dest_count + 10]
    # format word
    # title node names
    location = location.title()
    origin = origin.title()
    destination = destination.title()
    # replace "/" with "-"
    if "/" in location:
        location = location.replace("/", "-")
        last_letter = location[-1].upper()
        location = location[:-1] + last_letter
    if "/" in origin:
        origin = origin.replace("/", "-")
        last_letter = origin[-1].upper()
        origin = origin[:-1] + last_letter
    if "/" in destination:
        destination = destination.replace("/", "-")
        last_letter = destination[-1].upper()
        destination = destination[:-1] + last_letter
    return location, origin, destination, convoy_boolean