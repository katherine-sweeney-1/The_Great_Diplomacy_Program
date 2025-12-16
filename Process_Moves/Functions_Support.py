import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes/Class_Sub_Node"))
from Class_Sub_Node import Coastal_Node
from Functions_Attack import get_attack_outcome

def get_valid_support(commands, command):
    command_id = command.unit.id
    command_success = True
    # make sure supported attack is actually supporting an attack (ie another move does that attack)
    for cut_attempt in commands:
        command_success = True
        # check if unit supports an attack on support's brethren units
        if command.destination.is_occupied:
            # supports for attacks must have a corresponding attacking order
            if command.location != command.origin and command.origin != command.destination:
                supported_command_id = command.origin.is_occupied.id
                supported_command = commands[supported_command_id]
                # support is unsuccessful if supported attack ends up holding
                """
                if supported_command.location == supported_command.origin and supported_command.origin == supported_command.destination:
                    print(2, command_id, supported_command_id)
                    print(command.location.name, command.origin.name, command.destination.name)
                    print(supported_command.location.name, supported_command.origin.name, supported_command.destination.name)
                    command_success = False
                    break
                """
                # support is unsuccessful is supported attack does not match support
                if supported_command.location == supported_command.origin and supported_command.origin != supported_command.destination:
                    if command.origin != supported_command.origin or command.destination != supported_command.destination:
                        # make sure this works for all the moves
                        #if supported_command.location == supported_command.origin and supported_command.origin != supported_command.destination:
                        command_success = False
                        break
                        #else:
                            #command_success = True
            # support does not work if it supports an attack on a unit in its own country
            # if support command supports an attack from another country to its own country's unit
            if command.location.is_occupied.commander.human == command.destination.is_occupied.commander.human and command.origin != command.destination:
                destination_command_id = command.destination.is_occupied.id
                destination_command = commands[destination_command_id]
                if destination_command.origin == destination_command.destination:
                    command_success = False
                    break
                supported_command_id = command.origin.is_occupied.id
                supported_command = commands[supported_command_id]
                if supported_command.location.is_occupied.commander.human != destination_command.location.is_occupied.commander.human:
                    command_success = False
                    break
                if supported_command.location.is_occupied.commander.human == destination_command.location.is_occupied.commander.human:
                    # support for attack cannot happen if destination command is in its own country and holds
                    if destination_command.location == destination_command.origin and destination_command.origin == destination_command.destination:
                        command_success = False
                        break
                    # support for attack cannot happen if destination command is in its own country and supports a hold
                    elif destination_command.location != destination_command.origin:
                        command_success = False
                        break
            # if support command supports an attack from another country to that other country's unit
            elif command.origin.is_occupied.commander.human == command.destination.is_occupied.commander.human and command.origin != command.destination:
                destination_command_id = command.destination.is_occupied.id
                destination_command = commands[destination_command_id]     
                if destination_command.origin == destination_command.destination:
                    command_success = False
                    break      
                supported_command_id = command.origin.is_occupied.id
                supported_command = commands[supported_command_id]
                if supported_command.location.is_occupied.commander.human == destination_command.location.is_occupied.commander.human:
                    # need to make sure this change works for all the moves
                    if destination_command.location == destination_command.origin and destination_command.origin != destination_command.destination:
                        command_success = True
                    else:
                        command_success = False
                        break
            # get occupying unit for coastal nodes
            if isinstance (command.destination, Coastal_Node):
                command.destination.is_occupied.id = command.destination.sibling.is_occupied.id
            if command.destination.is_occupied in command.human.unit_members.keys():
                if command.origin != command.destination:
                    command_success = False
                    break
        # check if there is an attempt to cut support
            if command.location == commands[cut_attempt].destination and commands[cut_attempt].location == commands[cut_attempt].origin:
                # check if cut attempt has its own support
                if commands[cut_attempt].location == commands[cut_attempt].origin and commands[cut_attempt].origin != commands[cut_attempt].destination and command.destination.is_occupied == True: 
                    destination_id = command.destination.is_occupied.id
                    destination_command = commands[destination_id]
                    if commands[cut_attempt].destination == destination_command.location:       
                        command_success = check_cut_attempt_on_support(commands, command_id, cut_attempt)
                    else:
                        command_success = True
                else:
                    command_success = check_cut_attempt_on_support(commands, command_id, cut_attempt)
                if command_success == False:
                    break
        elif command.location == commands[cut_attempt].destination and commands[cut_attempt].location == commands[cut_attempt].origin:
            # check if cut attempt has its own support
            command_success = check_cut_attempt_on_support(commands, command_id, cut_attempt)
        if command_success == False:
            break
    return command_success

# check if the support is cut
def check_cut_attempt_on_support(commands, command_id, cut_support_id):
    for cutting_support_id in commands:
        # if the cut attempt (cut_support_id) has its own support (cutting_support_id)
        if cutting_support_id != command_id and cutting_support_id != cut_support_id and commands[cutting_support_id].origin:
            # check if the the support (cutting_support_id) supports the cut attempt's (other_id) attack
            if commands[cut_support_id].origin == commands[cutting_support_id].origin and commands[cutting_support_id].destination == commands[cut_support_id].destination:
                if commands[command_id].location == commands[cutting_support_id].destination:
                    for attack_on_cut_support_id in commands:
                        if commands[attack_on_cut_support_id].destination == commands[cutting_support_id].location:
                            command_success = False
                            break
                        else:
                            command_success = True
                else:
                    command_success = True
        # if the cut attempt does not have support
        else:
            # if support is for an attack on cut attempt
            command_success = is_support_for_attacking_cut(commands, command_id, cut_support_id)
            if command_success == False:
                break
            else:
                continue
    return command_success

def is_support_for_attacking_cut(commands, command_id, other_id):
    for supporting_attack in commands:
        if supporting_attack != command_id and supporting_attack != other_id:# and commands[supporting_attack].human == commands[command_id].human:
            # if the support is supporting an attack on the other_id's location
            if commands[supporting_attack].origin == commands[other_id].origin and commands[supporting_attack].destination == commands[supporting_attack].destination and commands[command_id].destination == commands[supporting_attack].location:
                command_success = False
            if commands[supporting_attack].origin == commands[command_id].origin and commands[supporting_attack].destination == commands[command_id].destination and commands[supporting_attack].destination == commands[other_id].location:
                command_success = True
                for supported_attack_on_support in commands:
                    if supported_attack_on_support != command_id and supported_attack_on_support != other_id and supported_attack_on_support != supporting_attack:
                        if commands[supported_attack_on_support].origin == commands[other_id].origin and commands[supported_attack_on_support].destination == commands[other_id].destination:
                            support_strength = 0
                            attacking_cut_strength = 0
                            for supporting_support_id in commands:
                                supporting_support = commands[supporting_support_id]
                                # get supports for the support being analyzed
                                if supporting_support_id != command_id:
                                    if supporting_support.origin == supporting_support.destination and supporting_support.origin == commands[command_id].location:
                                        supporting_support_success = get_valid_support(commands, supporting_support)
                                        if supporting_support_success == True:
                                            support_strength += 1
                            # get supports for the cutting attack
                            for attacking_support_id in commands:
                                attacking_support = commands[attacking_support_id]
                                if attacking_support != other_id and attacking_support != command_id:
                                    if attacking_support.origin == commands[other_id].origin and attacking_support.destination == commands[other_id].destination:
                                        attacking_support_success = get_valid_support(commands, attacking_support)
                                        if attacking_support_success == True:
                                            attacking_cut_strength += 1
                            if support_strength >= attacking_cut_strength:
                                command_success = True
                                break
                            else:
                                command_success = False
                                break    
                        else:
                            command_success = True
                if command_success == True:
                    break
            else:
                command_success = False
        else:
            command_success = False
    return command_success

def get_command_strength(commands, command, command_success):
# if the support affects another command (ie if there is a unit on the origin), get the supported command
    if command_success and command.origin.is_occupied != False:
        # get supported command for coastal territory
        if command.origin.is_occupied == 1:
            origin = command.origin
            for potential_supported_id in commands:
                if commands[potential_supported_id] == origin:
                    supported_command_id = commands[potential_supported_id].origin.is_occupied.id
                    break
        # get supported command for non-coastal territory
        else:
            supported_command_id = command.origin.is_occupied.id
        supported_command = commands[supported_command_id]
        # assign strength to the supported command
        if supported_command_id in commands:
            if supported_command.location != command.location:
                if command.origin and supported_command.origin and supported_command.destination == command.destination:
                    command_strength = 1
                    supported_command.cmd_strength(command_strength)
                elif supported_command.origin != supported_command.destination and supported_command.location != supported_command.origin:
                    command_strength = 1
                    supported_command.cmd_strength(command_strength)
                elif supported_command.origin == supported_command.destination and supported_command.location != supported_command.origin:
                    command_strength = 1
                    supported_command.cmd_strength(command_strength)
                else:
                    command_strength = 0
            else:
                command_strength = 0
        else:
            command_strength = 0
    # strength of zero if the supporting command does not affect another command
    else:
        command_strength = 0
    return commands


def get_success_supports(commands, id = None, recur_bool = None):
    for command_id in commands:
        command = commands[command_id]
        #if command_id == "IT04":
        #    print("IT04", command.location.name, command.origin.name, command.destination.name)
        #    print(" ")
        # if a unit is attacking
        if commands[command_id].location == commands[command_id].origin:
            continue
        command = commands[command_id]
        # if a unit is supporting
        if command.location != command.origin:
            command_success = get_valid_support(commands, command)
        commands = get_command_strength(commands, command, command_success)
        command.success(command_success)
    return commands