import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import assign_occupied

# get outcome locations for processed commands
def get_outcome_nodes(commands, nodes, processed_units):
    for command_id in commands:
        command = commands[command_id]
        displacing_attack = False
        # get outcomes for successful commands
        if command.location == command.origin and command.origin != command.destination and command.convoy == False:
            if command.succeed == True:
            #print("UESSSS", command_id, command.location.name, command.destination.name)
                retreat = False
                outcome_node = command.destination
            else:
                displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
            #print("YESSS 0", command_id, command.location.name, command.destination.name, outcome_node.name)
        elif command.location == command.origin and command.origin == command.destination:
            #print(1, command_id)
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        elif command.location != command.origin:
            #print(2, command_id)
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)
        # get outcomes for supports, holds, and unsuccessful attacks
        else:
            displacing_attack, outcome_node, retreat = check_displacement_attacks(command, command_id, commands)

        #print(command_id, units[command_id].location.name, outcome_node.name)
        #processed_units[command_id].assign_retreat_disband(retreat)
        #print("check 1", units[command_id].location.name, outcome_node.name)
        #print("check 1", processed_units[command_id].location.name)
        
        processed_units[command_id].assign_location(outcome_node, False, False)
        
        #print("check 2", processed_units[command_id].location.name, outcome_node.name)
        command.assign_outcome_location(outcome_node)
        #print("test outcome node", command.location.name)
        #print(" ")
        #if displacing_attack != False:
         #   print("displacing attack", command_id, displacing_attack)
        command.assign_displacing_attack(displacing_attack)
        #if command.displacing_attack != False:
         #   print("dipslacing attack 2", command.displacing_attack.unit.id)
        command.assign_retreat_disband(retreat)
        print(command.retreat)
    return commands, processed_units


def check_displacement_attacks(command, command_id, commands):
    displacing_attack = False
    # determine if any commands displace the unsuccessful command
    for potential_attack_id in commands:
        potential_attack = commands[potential_attack_id]
        if potential_attack_id != command_id:
            if potential_attack.destination.name == command.location.name:
                if potential_attack.location == potential_attack.origin and potential_attack.origin != potential_attack.destination:
                    if potential_attack.strength > command.strength and potential_attack.succeed == True:
                        outcome_node = command.location
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
            outcome_node = command.location
    return displacing_attack, outcome_node, retreat


# get retreat nodes for processed commands
def get_retreats(processed_commands, processed_nodes, processed_units):
    for unit_id in processed_units:
        unit = processed_units[unit_id]
        command = processed_commands[unit_id]
        if command.retreat == True:
            """
            command.unit.outcome_location.neighbors
            retreat_options = []
            
            for neighbor_id in neighbors:
            """
            neighbors = unit.location.neighbors
            retreat_options = []
            for neighbor_id in neighbors:
                neighbor = neighbors[neighbor_id]
                if neighbor.is_occupied:
                    pass
                else:
                    if command.displacing_attack == False or neighbor != command.displacing_attack.location:
                        #print("YESSSS", unit_id, neighbor.name, neighbor.is_occupied)
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

    for unit_id in units:
        unit = units[unit_id]
        unit.assign_original_location(unit.location)
    processed_commands, processed_units = get_outcome_nodes(processed_commands, processed_nodes, processed_units)
    
    processed_nodes, processed_units = assign_occupied(nodes, processed_units)

    processed_units = get_retreats(commands, processed_nodes, processed_units)

    for unit_id in processed_units:
        if commands[unit_id].retreat:
            print("check", unit_id, commands[unit_id].location.name, commands[unit_id].retreat)

            #print(retreat_choice)
            if commands[unit_id].retreat != False and len(commands[unit_id].retreat_nodes) > 0:
                retreat_choice = commands[unit_id].retreat_nodes[0]
                retreat_node = processed_nodes[retreat_choice]
                processed_units[unit_id].assign_location(retreat_node, False, False)
            else:
                retreat_choice = False
    return processed_nodes, nodes, processed_units, units


"""

Issue => game 8 spring 1902 shows GE02 (location Holland) can retreat to only Ruh when it can only retreat to Kie 

"""