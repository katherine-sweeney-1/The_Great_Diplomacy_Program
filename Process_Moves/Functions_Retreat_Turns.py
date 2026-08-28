import copy
import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied
from Functions_Post_Outcome import assign_unit_location

def assign_location_for_non_retreats(command, command_id, processed_units):
    if command.location == command.origin and command.origin != command.destination and command.convoy == False:
        # successful attacks have their location become the original command's destination
        if command.succeed == True:
            processed_units[command_id].assign_location(command.destination, False, False)
        # unsuccessful attacks that do not retreat remain on their location
        else:
            processed_units[command_id].assign_location(command.location, False, False)
    # supports, holds, and convoys that do not retreat remain on their location
    else:
        processed_units[command_id].assign_location(command.location, False, False)
    return processed_units

def get_retreats_from_input(processed_commands, processed_nodes):
    for command_id in processed_commands:
        command = processed_commands[command_id]
        if command.needs_retreat == True and len(command.retreat_nodes) > 0:
            print("choose a retreat option: ", command_id, command.retreat_nodes)
            retreat_node_string = input()
            if retreat_node_string in processed_nodes.keys():
                retreat_node = processed_nodes[retreat_node_string]
                command.assign_chosen_retreat(retreat_node)
            else:
                command.assign_chosen_retreat(False)
        else:
            command.assign_chosen_retreat(False)
    return processed_commands

def update_processed_commands(processed_commands, processed_nodes, processed_units):
    eliminated_commands_ids = []
    for command_id in processed_commands:
        if command_id not in processed_units.keys():
            #print(command_id)
            eliminated_commands_ids.append(command_id)
    for each_id in eliminated_commands_ids:
        processed_commands.pop(each_id)
    for command_id in processed_commands:
        command = processed_commands[command_id]
        location_string = processed_units[command_id].location.name
        if command.chosen_retreat != False:
            chosen_retreat_string = command.chosen_retreat.name
            command.assign_location(command.location.name, processed_nodes)
            command.assign_origin(command.location.name, processed_nodes)
            command.assign_destination(chosen_retreat_string, processed_nodes)
        else:
            location_string = processed_units[command_id].location.name
            command.assign_location(location_string, processed_nodes)
            command.assign_origin(location_string, processed_nodes)
            command.assign_destination(location_string, processed_nodes)
    return processed_commands


def run_retreat_turns(commands, commanders, nodes, units):
    processed_commands = copy.deepcopy(commands)
    processed_commanders = copy.deepcopy(commanders)
    processed_nodes = copy.deepcopy(nodes)
    processed_units = copy.deepcopy(units)
    """
    processed_commands = commands.copy()
    processed_commanders = commanders.copy()
    processed_nodes = nodes.copy()
    processed_units = units.copy()
    """
    processed_commands = get_retreats_from_input(processed_commands, processed_nodes)
    #print("before anything", processed_units)
    processed_units = assign_unit_location(processed_commands, processed_units, True)
    #print("assign unit location", processed_units)
    """
    for unit_id in processed_units:
        print("units before assign occupied", unit_id, processed_units[unit_id].location.name, processed_units[unit_id].location)
    print(processed_units)
    print(" ")
    """
    processed_nodes, processed_units = assign_occupied(processed_nodes, processed_units)
    #print("assign occupied", processed_units)
    """
    for node_id in processed_nodes:
        print("nodes", node_id, nodes[node_id].is_occupied)
        print("processed_nodes", node_id, processed_nodes[node_id].is_occupied)
    """
    processed_commands = update_processed_commands(processed_commands, processed_nodes, processed_units)
    
    for command_id in processed_commands:
        print(command_id, processed_commands[command_id].destination.name)
        print(command_id, processed_units[command_id].location.name)
    
    for node_id in processed_nodes:
        print("checking outside nodes functions", node_id, processed_nodes[node_id].is_occupied)
    
    return processed_commands, processed_commanders, processed_nodes, processed_units



"""

    Need to update commanders

    CHECK: do nodes and units get properly updated? Compare nodes and units before and after update

    need to incorporate special coasts

    Chosen retreats that choose disband are disbanded 

    Fix at the end: Change command.retreat_nodes to command.retreat_node_strings

    Fix at the end: Issue with 1904 Spring and input for non-node => disbands show up on map with >

"""


"""

GAME 8 

    - SPRING 1904 SHOULD HAVE NO RETREAT OPTIONS AND SHOULD DISBAND FOR ALL THREE UNITS

    - FALL 1904 KIE NEEDS TO DISBAND

    - FALL 1905 HOL NEEDS TO DISBAND

    - SPRING 1911 BRE NEEDS TO DISBAND

    - FALL 1912 MOS NEEDS TO DISBAND

    - SPRING 1913 RUH NEEDS TO DISBAND

    - FALL 1913 SIL NEEDS TO DISBAND

    - SPRING 1914 WES NEEDS TO DISBAND

    - FALL 1914 MAR NEEDS TO DISBAND

NEED TO DEBUG if two units only have one retreat option

    - units of same country

    - units of different countries

    - e.g. game 8 fall 1914

"""