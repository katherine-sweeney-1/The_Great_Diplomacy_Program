import sys
import os
sys.path.append(os.path.join("/The-Great-Diplomacy-Program/Nodes/Class_Sub_Node"))
from Class_Sub_Node import Coastal_Node

def check_other_attacks(command_id, command, commands, destination_command_id, count = None):
    if command.success == True or command.success == False:
        outcome = command.success
    # get a dictionary without the command to check if there are other attacking commands
    else:
        relevant_attacking_commands = {}
        # remove the command for the unit on the destination
        if destination_command_id != False:
            relevant_attacking_commands[command_id] = command
            destination_command = commands[destination_command_id]
            relevant_attacking_commands[destination_command_id] = destination_command
            relevant_attacking_commands = get_relevant_attacks(command_id, destination_command_id, commands, relevant_attacking_commands)
            last_relevant_attack = retrieve_last_relevant_attack(relevant_attacking_commands)
            # determine if command has a higher strength than other attacks
            if len(relevant_attacking_commands) > 2:
                for relevant_attack_id in relevant_attacking_commands:
                    one_attacking_command = relevant_attacking_commands[relevant_attack_id]
                    if len(relevant_attacking_commands) > 3 and one_attacking_command != command:
                        if command.strength > one_attacking_command.strength:
                            outcome = True
                        else:
                            destination_command = commands[destination_command_id]
                            # destination command attacks one attacking command and if destination command beats one attacking command, then command wins
                            if destination_command.location == destination_command.origin and destination_command.destination == one_attacking_command.location:
                                if destination_command.strength > one_attacking_command.strength:
                                    outcome = True
                                else:
                                    last_relevant_attack_outcome = get_attack_outcome (destination_command_id, destination_command, commands)
                                    if last_relevant_attack_outcome == False:
                                        if command.human == last_relevant_attack.human:
                                            outcome = False
                                            break
                                        else:
                                            if command.strength > last_relevant_attack.strength:
                                                outcome = True
                                            else:
                                                outcome = False
                                                break
                            # destination command does not attack one attacking command
                            else:
                                last_relevant_attack = retrieve_last_relevant_attack(relevant_attacking_commands)
                                # check command and destination command strengths if there are no last relevant attacks
                                if last_relevant_attack == None:
                                    if command.strength > destination_command.strength:
                                        outcome = True
                                    else:
                                        outcome = False
                                        break
                                # get attack outcome for last relevant attack
                                else:
                                    last_relevant_attack_outcome = get_attack_outcome (last_relevant_attack.unit.id, last_relevant_attack, commands)
                                    if last_relevant_attack_outcome == False:
                                        if command.human == last_relevant_attack.human:
                                            outcome = False
                                            break
                                        else:
                                            if command.strength > last_relevant_attack.strength:
                                                outcome = True
                                            else:
                                                outcome = False
                                                break
                                    # look for other attacks on destination and check those attacks on destination 
                                    else:
                                        for other_command_id in commands:
                                            other_command = commands[other_command_id]
                                            if other_command != command_id and command.destination == other_command.destination:
                                            # another attack on destination => check other attacks
                                                if command.destination.is_occupied:
                                                    destination_unit_id = command.destination.is_occupied.id
                                                    destination_command = commands[destination_unit_id]
                                                    if other_command != destination_command:
                                                        outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)
                                                    else:
                                                    # error with check if other attack is on destination function
                                                        outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                                                else:
                                                    outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                                                if outcome == False:
                                                    break 
                                            else:
                                                outcome = True
                    # there are only two relevant attacks involved (destination command and one other command)
                    else:
                        for other_relevant_command_id in commands:
                            other_relevant_command = commands[other_relevant_command_id]
                            # another attack on destination => check other attacks
                            if other_relevant_command.location == other_relevant_command.origin and other_relevant_command.origin != other_relevant_command.destination:
                                if command.destination.is_occupied:
                                    destination_unit_id = command.destination.is_occupied.id
                                    destination_command = commands[destination_unit_id]
                                    if other_relevant_command != destination_command and other_relevant_command.destination == command.destination and command != other_relevant_command and other_relevant_command.origin != other_relevant_command.destination:
                                        outcome = check_if_other_attack_is_on_destination(command_id, command, other_relevant_command, destination_command)
                                    else:
                                        # error with check if other attack is on destination function
                                        outcome = True
                                    if outcome == False:
                                        break
                                else:
                                    # error with check if other attack is on destination function
                                    outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                            else:
                                outcome = True
                            if outcome == False:
                                break 
                        if outcome == False:
                            break  
            # if there is only one relevant attack (i.e. destination command)
            else:
                # the command and destination command attack each other
                if destination_command.location == command.destination and destination_command.destination == command.location:
                    if command.strength > destination_command.strength:
                        outcome = True
                    else:
                        outcome = False
                # the command and destination command do not attack each other
                else:
                    last_relevant_attack = retrieve_last_relevant_attack(relevant_attacking_commands)
                    if last_relevant_attack == None:
                        if command.strength > destination_command.strength:
                            outcome = True
                        else:
                            outcome = False
                    else:
                        last_relevant_attack_outcome = get_attack_outcome (last_relevant_attack.unit.id, last_relevant_attack, commands)
                        # if last relevant outcome is false, attack only needs a strength of 2 to beat it (failed attack has strength 1)
                        if last_relevant_attack_outcome == False:
                            if command.human == destination_command.human:
                                outcome = False
                            else:
                                if command.strength > 1:
                                    outcome = True
                                else:
                                    outcome = False
                        else:
                            outcome = True
                                
        # check if another command attacks the same destination as the command in question
        else:
            for relevant_attack_id in commands:
                relevant_attack = commands[relevant_attack_id]
                # another attack on destination => check other attacks
                if command.destination.is_occupied:
                    destination_unit_id = command.destination.is_occupied.id
                    destination_command = commands[destination_unit_id]
                    if relevant_attack.destination == command.destination and relevant_attack.location == relevant_attack.origin and relevant_attack.origin != relevant_attack.destination:
                        outcome = check_if_other_attack_is_on_destination(command_id, command, relevant_attack, destination_command)
                    else:
                        if command.strength > destination_command.strength:
                            outcome = True
                        else:
                            outcome = False
                    if outcome == False:
                        break
                else:
                    if relevant_attack.destination == command.destination and relevant_attack != command:
                        if relevant_attack.location == relevant_attack.origin and relevant_attack.origin != relevant_attack.destination:
                    # error with check if other attack is on destination function
                            outcome = check_if_other_attack_is_on_destination(command_id, command, relevant_attack)
                        else:
                            outcome = True
                    else:
                        outcome = True
                if outcome == False:
                    break
        command.success(outcome)
        command.checking_other_attacks(True)
        return command.succeed

def check_if_other_attack_is_on_destination(command_id, command, other_attacking_command, destination_command = None):
    if other_attacking_command.destination == command.destination:
        # if the other command is attacking
        if other_attacking_command.origin != command.origin:
            # if the other command is attacking on an occupied territory
            if destination_command != None:
                # if the destination command is being attacked by other command and is not attacking (i.e. hold or support)
                if destination_command.destination == other_attacking_command.origin and destination_command.origin == destination_command.location:
                    if other_attacking_command.strength > destination_command.strength:
                        outcome = False
                    else:
                        outcome = True
                else:
                    if command.strength > other_attacking_command.strength:
                        outcome = True
                    else:
                        outcome = False
            else:
                """
                code might be redundant here
                """
                if command.strength > other_attacking_command.strength:
                    outcome = True
                else:
                    if command.strength > other_attacking_command.strength:
                        outcome = True
                    elif command.strength == other_attacking_command.strength and command.location == command.destination:
                        outcome = False
                    else:
                        outcome = False
        else:
            outcome = True
    else:
        outcome = True
    return outcome

def get_attack_outcome(command_id, command, commands, count = None):
    if command.location != command.origin:
        outcome = command.success 
    else:
        if command.destination.is_occupied != False:
            # get the command for the unit on the destination
            destination_command_id, destination_command = get_destination(command, commands)
            # if the unit on the destination is attacking 
            if destination_command.location == destination_command.origin and destination_command.destination != destination_command.origin:
                # if the command and unit on destination are trying to attack each other
                if command.location == destination_command.destination and command.destination == destination_command.location:
                    outcome = False
                    destination_command_outcome = False
                # if they're not attacking each other, get the outcome for the command on the destination
                else:
                    if count == None:
                        destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 1)
                    else:
                        if destination_command.location == command.destination and destination_command.destination == command.location:
                            destination_command_outcome = False
                        elif destination_command.destination != command.location:
                            destination_command_outcome = True
                        else:
                            destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 2)
                # if destination's command is successful, check for other attacks on the destination
                if destination_command_outcome:
                    other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                    outcome = other_attacks_on_destination_outcome
                # if the destination's command is not successful, check the strength of the command and destination command
                # ensure the commands have different commanders
                else:
                    if command.strength > 1:
                        outcome = check_commanders(command_id, command, commands, destination_command)
                    else:
                        outcome = False
            # if the unit on the destination is not attacking, check the strength to see if the unit is dislodged
            # ensure the commands have different commanders 
            else:

                if command.strength > destination_command.strength:
                    outcome = check_commanders(command_id, command, commands, destination_command)
                else:
                    outcome = False
        else:
            outcome = check_other_attacks(command_id, command, commands, False)
        command.success(outcome)
    return command.succeed

def get_hold_outcome(command_id, command, commands):
    # check for other attacks that affect the hold
    other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, False)
    # if there are no other attacks then the hold is valid
    if other_attacks_on_destination_outcome:
        outcome = True
    # if there are other attacks check the strengths of the attack(s) and the hold
    else:
        dictionary_without_command = commands.copy()
        dictionary_without_command.pop(command_id)
        for attacking_command_id in dictionary_without_command:
            attacking_command = dictionary_without_command[attacking_command_id]
            if attacking_command.location == attacking_command.origin and attacking_command.destination == command.location:
                if command.strength >= attacking_command.strength:
                    outcome = True
                else:
                    outcome = False
                    break
            else:
                outcome = True
    command.success(outcome)
    return command.succeed

def check_commanders(command_id, command, commands, destination_command):
    # if the two commands have the same human then the outcome is false
    # a command cannot dislodge a unit of the same country
    if command.human == destination_command.human:
        outcome = False
    else:
        # might need to check for other attacks
        destination_command_id = destination_command.unit.id
        outcome = check_other_attacks(command_id, command, commands, destination_command_id)
    return outcome

def get_destination(command, commands):
    destination_command_id = command.destination.is_occupied.id
    destination_command = commands[destination_command_id]
    return destination_command_id, destination_command

def get_success_attacks(commands):
    for command_id in commands:
        command = commands[command_id]
    for command_id in commands:
        command = commands[command_id]
        if command.location == command.destination:
            get_hold_outcome(command_id, commands[command_id], commands)
        elif command.location == command.origin and command.origin != command.destination:
            get_attack_outcome(command_id, commands[command_id], commands)
        # if not an attack or hold then continue to next command
        else:
            continue
    return commands


def get_relevant_attacks(command_id, destination_command_id, commands, relevant_attacking_commands, last_relevant_attack = None):
    command = commands[command_id]
    destination_command = commands[destination_command_id]
    # get relevant_attacks
    for relevant_attack_command_id in commands:
        relevant_attack_command = commands[relevant_attack_command_id]
        if command_id != relevant_attack_command_id and destination_command_id != relevant_attack_command_id and relevant_attack_command_id not in relevant_attacking_commands.keys():
            if relevant_attack_command.destination == destination_command.location and relevant_attack_command.location == relevant_attack_command.origin:
                relevant_attacking_commands[relevant_attack_command_id] = commands[relevant_attack_command_id]
                boolean_value = True
                relevant_other_command_id = relevant_attack_command_id
                break
            elif relevant_attack_command.location == commands[destination_command_id].destination and relevant_attack_command.location == relevant_attack_command.origin:
                relevant_attacking_commands[relevant_attack_command_id] = relevant_attack_command
                relevant_other_command_id = relevant_attack_command_id
                boolean_value = True
                break
            else:
                boolean_value = False
    # get relevant attacks for the relevant attack (recursion)
    if boolean_value == True:
        relevant_attacking_commands = get_relevant_attacks(destination_command_id, relevant_other_command_id, commands, relevant_attacking_commands)
    return relevant_attacking_commands

def retrieve_last_relevant_attack(relevant_attacking_commands):
    relevant_attack_destination_dict = {}
    # get dictionary of commands and their destinations
    for relevant_attack_id in relevant_attacking_commands:
        relevant_attacking_command = relevant_attacking_commands[relevant_attack_id]
        relevant_attack_destination_dict[relevant_attacking_command] = relevant_attacking_command.destination
    # retrieve last relevant attack from destinations 
    count = 0
    for relevant_attack_id in relevant_attacking_commands:
        relevant_attacking_command = relevant_attacking_commands[relevant_attack_id]
        if relevant_attacking_command.location in relevant_attack_destination_dict.values():# and relevant_attacking_command.destination not in relevant_attack_destination_dict.values():
            count +=1 
            last_relevant_attack = relevant_attacking_command
            break
        else:
            last_relevant_attack = None
    return last_relevant_attack