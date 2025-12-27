from Functions_Parse import determine_node_name

def parse_commands_and_units (txt):
    parsed_cmds = {}
    parsed_units = {}
    file = open(txt)
    lines = file.readlines()
    line_count = 0
    country = ""
    commander = ""
    for line in lines:
        line = line.replace("-", "to")
        stripped_line = ''.join([char for char in line if char.isalnum()])
        if len(stripped_line) > 0 and stripped_line[0] == "F":
             unit_type = "fleet"
        elif len(stripped_line) > 0 and stripped_line[0] == "A":
             unit_type = "army"
        # country --> get country and commander info
        if len(stripped_line) == 2:
            country = stripped_line
            commander = lines[line_count + 1]
            commander = ''.join([char for char in commander if char.isalnum()])
            unit_count = 1
        # command --> get success and fail status
        else:
            if stripped_line[-5:-1] == "FAIL":
                outcome = False
            else:
                outcome = True
        # commands --> get location, origin, and destination
        if stripped_line != commander and stripped_line != country and stripped_line != "":
            # unit name
            if unit_count > 9:
                unit_name = country + str(unit_count)
            else:
                unit_name = country + str(0) + str(unit_count)
            unit_count += 1
            loc_count = 0
            origin_count = 0
            dest_count = 0
            # if there is a coastal node
            if len(stripped_line) > 2 and "/" in line:
                # location is coastal
                if line[5] == "/":
                    loc_count = 3
                # origin is coastal, support
                if (line[7] == "S" or line[7] == "C") and line[13] == "/":
                    origin_count = 3
                    if "to" in line:
                        dest_count = 0
                    else:
                        dest_count = 3
                elif (line[6] == "S" or line[6] == "C") and line[11] == "/":
                    origin_count = 3
                    if "to" in line:
                        dest_count = 0
                    else:
                        dest_count = 3
                # attack, destination is coastal
                if line[6:8] == "to" and line[12] == "/":
                     dest_count = 3
                # support attack, destination is coastal:
                elif len(line) > 18 and line[18] == "/":
                     dest_count = 3
            location, origin, destination, convoy_boolean = determine_node_name(line, loc_count, origin_count, dest_count)
            parsed_cmds[unit_name] = {
                 "location": location,
                 "origin": origin,
                 "destination": destination,
                 "country": country,
                 "owner": commander,
                 "outcome": outcome,
                 "convoy": convoy_boolean
            }
            parsed_units[unit_name] = {
                 "type": unit_type,
                 "loc": location,
                 "country": country
            }
        line_count += 1
    return parsed_cmds, parsed_units