from Input_Commands_and_Commanders import input_data_1, input_data_2, input_data_3, input_data_4, input_data_5, input_data_6
from Input_Commands_and_Commanders import input_data_7, input_data_8, input_data_8b
import sys
sys.path.append("../The_Great_Diplomacy_Program/Parse")
from Parse_Objects import parse_commands_and_units
from Run_Objects import create_objects
from Run_Processing import run_processing
sys.path.append("../The_Great_Diplomacy_Program/Tables")
from Functions_Table import yield_table

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"
data_fleet_special_coastal = "data/Data_Ter_Fleet_Special_Coasts.csv"

#game_and_turn = "game1_1903_fall"

def run_main_original():
    cmdrs_data_list = cmdrs_3
    cmds = cmds_3a
    units_data_list = units_3a
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    db_table = yield_table(processed_commands)

def run_main_testing():
    commanders_data = cmdrs_2_1906
    parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, data_fleet_coastal, commanders_data, parsed_units, parsed_cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    #db_table = yield_table(processed_commands)


def run_main_unit_testing(input_data, game_number_string):
    count = 0
    turns_objects = {}
    for commands_data in input_data:
        objects = {}
        game_year = 1908 + count/2
        game_year = int(game_year)
        game_season = count % 2
        match game_season:
            case 0:
                game_season = "Spring"
            case 1:
                game_season = "Fall"
        game_season = game_season.lower()
        game_and_turn = str(game_number_string) + str(game_year) + "_" + game_season
        #print(game_and_turn)
        commanders_data = input_data[commands_data]
        parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
        commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, data_fleet_coastal, data_fleet_special_coastal, commanders_data, parsed_units, parsed_cmds)
        #print("Game 2 {} {}".format(game_year, game_season))
        nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
        """
        for command_id in commands:
            if commands[command_id].succeed == commands[command_id].predet_outcome and commands[command_id].legal == 1:
                print(command_id, "Correct outcome", commands[command_id].succeed)
            else:
                print("uh oh", command_id, commands[command_id].strength, commands[command_id].legal, commands[command_id].succeed)
        """
        db_table = yield_table(processed_commands, game_and_turn)
        #print(" ")
        count += 1
        objects["Commands"] = commands
        objects["Commanders"] = commanders
        objects["Nodes"] = nodes
        objects["Units"] = units
        turns_objects[game_and_turn] = objects
        #print(turns_objects)
    return turns_objects
        #return commands, commanders, nodes, units


#run_main_unit_testing(input_data_1)

"""

Game 1 starts at year 1903

Game 8b starts at year 1908


"""
