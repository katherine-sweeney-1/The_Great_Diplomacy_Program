import sys
sys.path.append("../The_Great_Diplomacy_Program/Parse")
from Parse_Objects import parse_commands_and_units
from Run_Objects import create_objects
from Run_Processing import run_processing
sys.path.append("../The_Great_Diplomacy_Program/Tables")
from Functions_Table import yield_table
sys.path.append("../The_Great_Diplomacy_Program/GUI")
from Functions_GUI import run_gui, retrieve_node_coordinates, assign_neighbor_coordinates
from flask import Flask

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"
data_fleet_special_coastal = "data/Data_Ter_Fleet_Special_Coasts.csv"

def run_tgdp(input_data, game_number_string, start_game_year, save_images_boolean):
    count = 0
    turns_objects = {}
    for commands_data in input_data:
        objects = {}
        game_year = int(start_game_year)
        game_year = game_year + count/2
        game_year = int(game_year)
        game_season = count % 2
        match game_season:
            case 0:
                game_season = "Spring"
            case 1:
                game_season = "Fall"
        game_and_turn_string = "Game" + str(game_number_string) + "_" + str(game_year) + "_" + game_season
        print(game_and_turn_string)
        commanders_data = input_data[commands_data]
        parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
        commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, data_fleet_coastal, data_fleet_special_coastal, commanders_data, parsed_units, parsed_cmds)
        #for node_id in nodes:
        #    print(node_id)
        commands, processed_commands, nodes, units = run_processing(commands, commanders, nodes, units)
        """
        for command_id in commands:
            command = commands[command_id]
            print(command.location.name, command.origin.name, command.destination.name)
        print(" ")
        """
        # retrieve nodes and units for winter season
        db_table = yield_table(processed_commands, game_and_turn_string)
        objects["Commands"] = commands
        objects["Commanders"] = commanders
        objects["Nodes"] = nodes
        objects["Units"] = units
        turns_objects[game_and_turn_string] = objects
        if game_season == "Fall":
            turns_objects = get_winter_objects(processed_commands, commanders, nodes, units, game_number_string, game_year, turns_objects)
        count += 1
    for game_and_turn_string in turns_objects:
        commands = turns_objects[game_and_turn_string]["Commands"]
    gui = run_gui(turns_objects, str(game_number_string), start_game_year, save_images_boolean)
    for command_id in processed_commands:
        processed_command = processed_commands[command_id]
        processed_command.location = units[command_id].location
    
"""

Game 1 starts at year 1903

Game 8b starts at year 1908

"""

def get_winter_objects(commands, commanders, nodes, units, game_number_string, game_year, turns_objects):
    disbanded_commands = {}
    for game_and_turn_string in turns_objects:
        commands = turns_objects[game_and_turn_string]["Commands"]
        for command_id in commands:
            command = commands[command_id]
    next_game_season = "Winter"
    winter_game_and_turn_string = "Game" + str(game_number_string) + "_" + str(game_year) + "_" + next_game_season
    for command_id in commands:
        winter_objects = {}
        command = commands[command_id]
        if command.succeed:
            if command.location == command.origin and command.origin != command.destination:
                command.assign_winter_location(command.destination)
            else:
                command.assign_winter_location(command.location)
        else:
            if command_id in units.keys():
                command.assign_winter_location(units[command_id].location)
            else:    
                command.assign_winter_location(False)
    winter_objects["Commands"] = commands
    winter_objects["Commands"] = commands
    winter_objects["Commanders"] = commanders
    winter_objects["Nodes"] = nodes
    winter_objects["Units"] = units
    winter_game_and_turn_string = "Game" + str(game_number_string) + "_" + str(game_year) + "_" + next_game_season
    turns_objects[winter_game_and_turn_string] = winter_objects
    return turns_objects

