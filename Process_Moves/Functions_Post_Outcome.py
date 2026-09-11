import copy
import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied

# Checks if unit is displaced by an attack
def check_displacement_attacks(command, command_id, commands):
    displacing_attack = False
    # determine if any commands displace the unsuccessful command
    for potential_attack_id in commands:
        potential_attack = commands[potential_attack_id]
        if potential_attack_id != command_id:
            if potential_attack.destination.name == command.location.name:
                if potential_attack.location == potential_attack.origin and potential_attack.origin != potential_attack.destination:
                    if potential_attack.succeed == True:
                        displacing_attack = potential_attack
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
    return displacing_attack, retreat

# Determines whether a unit needs to retreat 
def determine_if_retreats(commands):
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.origin and command.origin != command.destination and command.convoy == False:
            if command.succeed == True:
                displacing_attack = False
                retreat = False
                #outcome_node = command.destination
            else:
                displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
                #print(command_id, displacing_attack, retreat)
        elif command.location == command.origin and command.origin == command.destination:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location != command.origin:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        else:
            displacing_attack, retreat = check_displacement_attacks(command, command_id, commands)
        command.assign_displacing_attack(displacing_attack)
        command.assign_retreat_disband(retreat)
    return commands

# Determine the outcome nodes
# Assumes that input for retreats is already given (e.g. UK01 retreats to Den)
def check_valid_retreat_choice(command):
    for retreat_node in command.retreat_nodes:
        print(command.unit.id, retreat_node)
        if command.chosen_retreat.name == retreat_node:
            valid_retreat_choice = True
            break
        else:
            valid_retreat_choice = False
    return valid_retreat_choice

# Assign the new location for units that don't retreat based on the previous turn's outcome
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


# Assign the location for all units
# Includes units that retreat, units that disband, and units that do not retreat or disband
# Have retreats boolean: whether the retreats have been given yet
def assign_unit_location(commands, processed_units, have_retreats_boolean):
    for command_id in commands:
        command = commands[command_id]
        if have_retreats_boolean:
            if command.needs_retreat == True:
                if command.chosen_retreat != False:
                    valid_retreat_choice = check_valid_retreat_choice(command)
                    if valid_retreat_choice == True:
                        commands_length = len(commands)
                        count = 0
                        for other_command_id in commands:
                            other_command = commands[other_command_id]
                            if command != other_command and other_command.needs_retreat == True and other_command.chosen_retreat != False:
                                other_valid_retreat_choice = check_valid_retreat_choice(command)
                                if other_valid_retreat_choice == True:
                                    if command.chosen_retreat.name == other_command.chosen_retreat.name:
                                        processed_units.pop(command_id)
                                        break
                                    elif command.chosen_retreat.name != other_command.chosen_retreat.name and count == commands_length:
                                        processed_units[command_id].assign_location(command.chosen_retreat, False, False)
                            # might need to add units with same retreat choice disbands here
                    # if more than one comand has the same retreat option, the unit disbands
                    else:
                        processed_units.pop(command_id)
                else:
                    processed_units.pop(command_id)
            else:
                processed_units = assign_location_for_non_retreats(command, command_id, processed_units)
        else:
            processed_units = assign_location_for_non_retreats(command, command_id, processed_units)
    return processed_units



# Get retreat nodes for processed commands
def get_retreats(commands, nodes, units, processed_commands, processed_nodes, processed_units):
    for unit_id in processed_units:
        unit = processed_units[unit_id]
        command = processed_commands[unit_id]
        if command.needs_retreat == True:
            neighbors = unit.location.neighbors
            retreat_options = []
            for neighbor_id in neighbors:
                neighbor = processed_nodes[neighbor_id]
                #print(unit_id, neighbor.name)
                print(unit_id, neighbor.name, neighbor.is_occupied)
                if neighbor.is_occupied:
                    continue
                else:
                    """
                    displacing_attack_node = False
                    previously_occupied_neighbors = units[unit_id].location.neighbors
                    for previously_occupied_neighbor in previously_occupied_neighbors:
                        if neighbor.is_occupied:
                            possible_attack_unit = neighbor.is_occupied
                            possible_attack_id = possible_attack_unit.id
                            possible_attack = commands[possible_attack_id]
                            if possible_attack.location == possible_attack.origin and possible_attack.origin != possible_attack.destination:
                                if possible_attack.destination == command.location and possible_attack.succeed == True:
                                    displacing_attack_node = neighbor
                                    break
                    """
                    """
                    was neighbor occupied
                    was the occupying unit attacking
                    """
                    #print(unit_id, neighbor_id, command.displacing_attack.location.name, "uh")
                    if command.displacing_attack == False or neighbor != command.displacing_attack.location:
                        if unit.type == "army" and neighbor.node_type == "Land":
                            retreat_options.append(neighbor_id)
                        elif unit.type == "fleet" and neighbor.node_type == "Sea":
                            retreat_options.append(neighbor_id)
                        elif neighbor.node_type == "Coast":
                            retreat_options.append(neighbor_id)
            command.assign_retreat_nodes(retreat_options)
            print(unit_id, command.retreat_nodes)
    return processed_units

# Process outcomes
def process_outcomes(commands, commanders, nodes, units):
    have_retreats_boolean = False
    processed_commands = copy.deepcopy(commands)
    processed_commanders = copy.deepcopy(commanders)
    processed_nodes = copy.deepcopy(nodes)
    processed_units = copy.deepcopy(units)
    processed_commands = determine_if_retreats(processed_commands)
    processed_units = assign_unit_location(processed_commands, processed_units, False)
    #for unit_id in processed_units:
    #    print("check", unit_id, processed_units[unit_id].location.name)
    processed_nodes, processed_units = assign_occupied(processed_nodes, processed_units)
    """
    
    NEED TO ASSIGN OCCUPIED COASTAL
    
    """
    processed_units = get_retreats(commands, nodes, units, processed_commands, processed_nodes, processed_units)
    return processed_commands

"""

spring 1902 GE05 says Ven is a retreat option when the attack is from Ven
fall 1902 AU02 same issue
"""