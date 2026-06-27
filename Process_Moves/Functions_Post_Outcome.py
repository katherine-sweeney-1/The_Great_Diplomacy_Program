import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied

"""
# get outcome locations for processed commands
# takes processed commands and processed units as input
# creates processed commands and processed units with new information
def get_outcome_nodes(commands, processed_units):
    for command_id in commands:
        command = commands[command_id]
        displacing_attack = False
        if command.location == command.origin and command.origin != command.destination and command.convoy == False:
            if command.succeed == True:
                retreat = False
                outcome_node = command.destination
            else:
                displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location == command.origin and command.origin == command.destination:
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location != command.origin:
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        else:
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        processed_units[command_id].assign_location(outcome_node, False, False)
        command.assign_outcome_location(outcome_node)
        command.assign_displacing_attack(displacing_attack)
        command.assign_retreat_disband(retreat)
    return commands, processed_units

# check if unit is displaced by an attack
def check_displacement_attacks(command, command_id, commands):
    displacing_attack = False
    # determine if any commands displace the unsuccessful command
    for potential_attack_id in commands:
        potential_attack = commands[potential_attack_id]
        if potential_attack_id != command_id:
            if potential_attack.destination.name == command.location.name:
                if potential_attack.location == potential_attack.origin and potential_attack.origin != potential_attack.destination:
                    if potential_attack.succeed == True:
                        outcome_node = command.location
                        displacing_attack = potential_attack
                        retreat = True
                    #if potential_attack.strength > command.strength and potential_attack.succeed == True:        retreat = True
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
    return displacing_attack, outcome_node, retreat

# get retreat nodes for processed commands
def get_retreats(processed_commands, processed_nodes, processed_units):
    for unit_id in processed_units:
        unit = processed_units[unit_id]
        command = processed_commands[unit_id]
        if command.retreat == True:
            neighbors = unit.location.neighbors
            retreat_options = []
            for neighbor_id in neighbors:
                neighbor = processed_nodes[neighbor_id]
                if neighbor.is_occupied:
                    continue
                else:
                    if command.displacing_attack == False or neighbor != command.displacing_attack.location:
                        if unit.type == "army" and neighbor.node_type == "Land":
                            retreat_options.append(neighbor_id)
                        elif unit.type == "fleet" and neighbor.node_type == "Sea":
                            retreat_options.append(neighbor_id)
                        elif neighbor.node_type == "Coast":
                            retreat_options.append(neighbor_id)
            command.assign_retreat_nodes(retreat_options)
    return processed_units

# process outcomes
def process_outcomes(commands, nodes, units):
    processed_units = units.copy()
    processed_nodes = nodes.copy()
    processed_commands = commands.copy()
    #for unit_id in units:
    #    unit = units[unit_id]
    #    unit.assign_original_location(unit.location)
    processed_commands, processed_units = get_outcome_nodes(processed_commands, processed_units)
    processed_nodes, processed_units = assign_occupied(nodes, processed_units)
    processed_units = get_retreats(commands, processed_nodes, processed_units)
    for unit_id in processed_units:
        command = commands[unit_id]
        processed_unit = processed_units[unit_id]
        if command.retreat:
            if command.retreat == True and len(command.retreat_nodes) > 0:
                retreat_choice = command.retreat_nodes[0]
                retreat_node = processed_nodes[retreat_choice]
                processed_unit.assign_location(retreat_node, False, False)
    processed_units_with_disbands = processed_units.copy()
    for unit_id in processed_units:
        command = commands[unit_id]
        if command.retreat == True:
            if len(command.retreat_nodes) == 0:
                processed_commands.pop(unit_id)
                processed_units_with_disbands.pop(unit_id)
    return commands, processed_commands, nodes, processed_nodes, units, processed_units_with_disbands
"""


# get outcome locations for processed commands
# takes processed commands and processed units as input
# creates processed commands and processed units with new information
def determine_if_retreats(commands, units):
    for command_id in commands:
        command = commands[command_id]
        outcome_node = command.location
        #displacing_attack = False
        # CHECK: is command.convoy = False necessary? 
        if command.location == command.origin and command.origin != command.destination and command.convoy == False:
            if command.succeed == True:
                displacing_attack = False
                retreat = False
                outcome_node = command.destination
            else:
                displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location == command.origin and command.origin == command.destination:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location != command.origin:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        else:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        #units[command_id].assign_location(outcome_node, False, False)
        #command.assign_outcome_location(outcome_node)
        command.assign_displacing_attack(displacing_attack)
        command.assign_retreat_disband(retreat)
        if retreat == True:
            print(command_id, command.needs_retreat)
    return commands, units

# check if unit is displaced by an attack
def check_displacement_attacks(command, command_id, commands):
    displacing_attack = False
    # determine if any commands displace the unsuccessful command
    for potential_attack_id in commands:
        potential_attack = commands[potential_attack_id]
        if potential_attack_id != command_id:
            if potential_attack.destination.name == command.location.name:
                if potential_attack.location == potential_attack.origin and potential_attack.origin != potential_attack.destination:
                    if potential_attack.succeed == True:
                        #outcome_node = command.location
                        displacing_attack = potential_attack
                        retreat = True
                    #if potential_attack.strength > command.strength and potential_attack.succeed == True:        retreat = True
                        break
                    else:
                        retreat = False
                else:
                    retreat = False
            else:
                retreat = False
        else:
            retreat = False
            #outcome_node = command.location
    return displacing_attack, retreat

# get retreat nodes for processed commands
def get_retreats(processed_commands, processed_nodes, processed_units):
    for unit_id in processed_units:
        unit = processed_units[unit_id]
        command = processed_commands[unit_id]
        if command.needs_retreat == True:
            neighbors = unit.location.neighbors
            retreat_options = []
            for neighbor_id in neighbors:
                neighbor = processed_nodes[neighbor_id]
                if neighbor.is_occupied:
                    continue
                else:
                    if command.displacing_attack == False or neighbor != command.displacing_attack.location:
                        if unit.type == "army" and neighbor.node_type == "Land":
                            retreat_options.append(neighbor_id)
                        elif unit.type == "fleet" and neighbor.node_type == "Sea":
                            retreat_options.append(neighbor_id)
                        elif neighbor.node_type == "Coast":
                            retreat_options.append(neighbor_id)
            command.assign_retreat_nodes(retreat_options)
    return processed_units

"""

FOR RETREAT OBJECTS

    - Need to assign location: units.assign_location ()

    - Assign outcome node as location, origin, and destination for every non-retreat command

"""
# process outcomes
def process_outcomes(commands, nodes, units):
    processed_units = units.copy()
    processed_nodes = nodes.copy()
    processed_commands = commands.copy()
    #for unit_id in units:
    #    unit = units[unit_id]
    #    unit.assign_original_location(unit.location)
    commands, units = determine_if_retreats(commands, units)
    processed_nodes, processed_units = assign_occupied(nodes, processed_units)
    processed_units = get_retreats(commands, processed_nodes, processed_units)
    """
    for unit_id in processed_units:
        command = commands[unit_id]
        processed_unit = processed_units[unit_id]
        if command.needs_retreat:
            if command.needs_retreat == True and len(command.retreat_nodes) > 0:
                retreat_choice = command.retreat_nodes[0]
                retreat_node = processed_nodes[retreat_choice]
                processed_unit.assign_location(retreat_node, False, False)
    processed_units_with_disbands = processed_units.copy()
    for unit_id in processed_units:
        command = commands[unit_id]
        if command.needs_retreat == True:
            if len(command.retreat_nodes) == 0:
                processed_commands.pop(unit_id)
                processed_units_with_disbands.pop(unit_id)
    """
    return commands, processed_commands, nodes, processed_nodes, units, processed_units
    return commands, processed_commands, nodes, processed_nodes, units, processed_units_with_disbands
