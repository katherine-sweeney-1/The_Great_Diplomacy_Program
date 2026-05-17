import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied

# get outcome locations for processed commands
def get_outcome_nodes(commands, nodes, units):
    for command_id in commands:
        command = commands[command_id]
        # get outcomes for successful commands
        if command.succeed and command.location == command.origin and command.origin == command.destination:
            retreat = False
            outcome_node = command.destination
            """
            # outcome location for holds
            if command.location == command.origin == command.destination:

                outcome_node = command.destination
            # outcome location for attacks
            elif command.location == command.origin and command.origin != command.destination:
                outcome_node = command.destination
            # outcomes location for supports
            else:
                outcome_node = command.location
            retreat = False
            potential_attack = False
            """
        # get outcomes for supports, holds, and unsuccessful attacks
        else:
            # determine if any commands displace the unsuccessful command
            for potential_attack_id in commands:
                potential_attack = commands[potential_attack_id]
                if potential_attack_id != command_id:
                    if potential_attack.destination.name == command.location.name:
                        if potential_attack.location == potential_attack.origin and potential_attack.origin != potential_attack.destination:
                            if potential_attack.strength > command.strength:
                                outcome_node = command.location
                                retreat = True
                                break
                            else:
                                retreat = False
                        else:
                            retreat = False
                    else:
                        retreat = False
                else:
                    retreat = False
                    outcome_node = command.location
                if retreat == False:
                    potential_attack_ = False
        units[command_id].assign_retreat_disband(retreat)
        units[command_id].assign_location(outcome_node, False, False)
        command.assign_outcome_location(outcome_node)
    return commands, potential_attack, units

# get retreat nodes for processed commands
def get_retreats(commands, displacing_attack, units):
    for unit_id in units:
        if units[unit_id].retreat == True:
            neighbors = units[unit_id].location.neighbors
            retreat_options = []
            for neighbor in neighbors:
                if neighbors[neighbor].is_occupied:
                    pass
                else:
                    if displacing_attack != False:
                        print("CHECKING", unit_id, units[unit_id].location.name, displacing_attack.location.name)
                    if displacing_attack == False or neighbor != displacing_attack.location:
                        if units[unit_id].type == "army" and neighbors[neighbor].node_type == "Land":
                            retreat_options.append(neighbor)
                        elif units[unit_id].type == "fleet" and neighbors[neighbor].node_type == "Sea":
                            retreat_options.append(neighbor)
                        elif neighbors[neighbor].node_type == "Coast":
                            retreat_options.append(neighbor)
            units[unit_id].assign_retreat_disband(retreat_options)
    return units

# process outcomes
def process_outcomes(commands, nodes, units):
    processed_units = units
    processed_nodes = nodes
    processed_commands = commands
    processed_commands, displacing_attack, processed_units = get_outcome_nodes(processed_commands, processed_nodes, processed_units)
    """
    for unit_id in units:
        unit = units[unit_id]
        print("outcome location", unit_id, unit.location.name)
        print("command outcome location", commands[unit_id].outcome_location.name)
    """
    processed_nodes, processed_units = assign_occupied(processed_nodes, processed_units)
    #print(nodes)
    processed_units = get_retreats(processed_commands, displacing_attack, processed_units)
    for unit_id in processed_units:
        if processed_units[unit_id].retreat:
            print(unit_id, processed_units[unit_id].retreat)
            retreat_choice = processed_units[unit_id].retreat[0]
            print(retreat_choice)
            retreat_node = processed_nodes[retreat_choice]
            processed_units[unit_id].assign_location(retreat_node, False, False)
    return processed_nodes, nodes, processed_units, units


"""

Issue => game 8 spring 1902 shows GE02 (location Holland) can retreat to only Ruh when it can only retreat to Kie 

"""