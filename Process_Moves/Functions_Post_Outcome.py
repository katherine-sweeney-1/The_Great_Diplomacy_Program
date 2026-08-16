import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied

# get outcome locations for processed commands
# takes processed commands and processed units as input
# creates processed commands and processed units with new information
def determine_if_retreats(commands):
    for command_id in commands:
        command = commands[command_id]
        #outcome_node = command.location
        #displacing_attack = False
        # CHECK: is command.convoy = False necessary? 
        if command.location == command.origin and command.origin != command.destination and command.convoy == False:
            if command.succeed == True:
                displacing_attack = False
                retreat = False
                #outcome_node = command.destination
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
        #if retreat == True:
        #    print(command_id, command.needs_retreat)
    return commands

"""

determine the outcome nodes
assumes that input for retreats is already given (e.g. UK01 retreats to Den)

"""

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

def assign_unit_location(commands, processed_units, have_retreats_boolean):
    for command_id in commands:
        command = commands[command_id]
        if have_retreats_boolean:
            if command.needs_retreat == True:
                if command.chosen_retreat != False:
                    for retreat_node in command.retreat_nodes:
                        if command.chosen_retreat.name == retreat_node:
                            valid_retreat_choice = True
                            break
                        else:
                            valid_retreat_choice = False
                    if valid_retreat_choice == True:
                        processed_units[command_id].assign_location(command.chosen_retreat, False, False)
                    else:
                        processed_units.pop(command_id)
                else:
                    processed_units.pop(command_id)
            else:
                processed_units = assign_location_for_non_retreats(command, command_id, processed_units)
        else:
            processed_units = assign_location_for_non_retreats(command, command_id, processed_units)
    return processed_units

                
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

# command.retreat_nodes => gives options for retreats
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

# process outcomes
def process_outcomes(commands, commanders, nodes, units):
    have_retreats_boolean = False
    processed_commands = commands.copy()
    processed_commanders = commanders.copy()
    processed_nodes = nodes.copy()
    processed_units = units.copy()
    commands = determine_if_retreats(commands)
    processed_units = assign_unit_location(commands, processed_units, False)
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
    return commands

def process_retreat_turns(commands, commanders, nodes, units):
    processed_commands = commands.copy()
    processed_commanders = commanders.copy()
    processed_nodes = nodes.copy()
    processed_units = units.copy()
    processed_commands = get_retreats_from_input(processed_commands, processed_nodes)
    #print("before anything", processed_units)
    processed_units = assign_unit_location(processed_commands, processed_units, True)
    #print("assign unit location", processed_units)
    processed_nodes, processed_units = assign_occupied(processed_nodes, processed_units)
    #print("assign occupied", processed_units)
    processed_commands = update_processed_commands(processed_commands, processed_nodes, processed_units)
    #for command_id in processed_commands:
    #    print(command_id, processed_commands[command_id].location.name)
    return processed_commands, processed_commanders, processed_nodes, processed_units



"""
    next need to update commands location, origin, and destination align with units' location
    also need to remove commands that disband
    

    command.assign_location(self, location_string, nodes)

    
    Fix at the end: change command.retreat_nodes to command.retreat_node_strings

    Need to update commanders

    I think nodes and units are updated 

    add disband option for retreats

    need to incorporate special coasts

"""




"""

Issue with 1904 Spring and input for non-node => disbands show up on map with >

What I want 


    - Spring/Fall Retreat turn:

        - chosen retreats that choose disband are disbanded 

        - retreating commands have same location and origin and chosen retreat as destination

        - other commands have outcome node as location, origin, and destination

        - if multiple units retreat to the same territory, both disband for both units of the same country and of different countries
        
            - Game 8 Spring 1908

            - Game 8 Fall 1914

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

FOR RETREAT OBJECTS

    - Need to assign location: units.assign_location ()

    - Assign outcome node as location, origin, and destination for every non-retreat command

"""