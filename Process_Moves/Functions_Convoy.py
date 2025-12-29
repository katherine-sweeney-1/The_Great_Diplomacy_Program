import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

# filter fleets that convoy
def filter_convoyer(command):
    # Convoy must have a different origin, location, and destination
    if command.location != command.origin and command.location != command.destination and command.origin != command.destination and command.unit.type == "fleet":
        if command.origin.node_type == "Coast" and command.destination.node_type == "Coast":
            if command.location.node_type == "Sea":
                command.legal = 1
            else:
                command.legal = "False - convoy location is not a sea"
        else:
            command.legal = "False - convoy is not between coasts"
    else:
        command.legal = command.legal
    return command

#filter convoyed armies
def filter_convoyed_army (command, commands):
    if command.location == command.origin and command.origin != command.destination and command.unit.type == "army":
        for convoyer_command_id in commands:
            convoyer_command = commands[convoyer_command_id]
            if command != convoyer_command and command.origin == convoyer_command.origin and command.destination == convoyer_command.destination:
                if convoyer_command.legal == convoyer_command.legal:
                    command.legal = 1
                    break
                else:
                    command.legal = "False - convoyed army does not have a legally supporting convoy"
            else:
                command.legal = "False - convoyed army does not have a corresponding convoy"
    else:
        command.legal = command.legal
    return command

# filter supports for convoys
def filter_convoy_support (command, commands):
    if command.location != command.origin and command.origin != command.destination and command.legal != 1:
        for convoy_command_id in commands:
            convoy_command = commands[convoy_command_id]
            # check if there's a corresponding fleet convoying the command
            # check if the fleet convoy has a valid path 
            if convoy_command.legal == 1 and convoy_command.unit.type == "fleet" and convoy_command.origin.node_type == "Coast" and convoy_command.destination.node_type == "Coast":
                if command.location != convoy_command.location and command.origin == convoy_command.origin and command.destination == convoy_command.destination:
                    convoyer_fleet_boolean = True
                    break
                else:
                    convoyer_fleet_boolean = False
            else:
                convoyer_fleet_boolean = False
            # an army needs to be convoyed 
        for convoyed_command_id in commands:
            convoyed_command = commands[convoyed_command_id]
            if convoyed_command.legal == 1 and convoyed_command.unit.type == "army" and convoyed_command.origin.node_type == "Coast" and convoyed_command.destination.node_type == "Coast":
                if command.location != convoyed_command.location and command.origin == convoyed_command.origin and command.destination == convoyed_command.destination:
                    convoyed_army_boolean = True
                else:
                    convoyed_army_boolean = False
            else:
                convoyed_army_boolean = False
            if convoyer_fleet_boolean == True and convoyed_army_boolean == True:
                command.legal = 1
                break
    else:
        convoyer_fleet_boolean = False
        convoyed_army_boolean = False
        command.legal = command.legal
    return command

# filter valid paths for convoyed armies
def filter_valid_convoy_paths(command, commands):
        convoying_commands = {}
        convoying_commands[command.unit.id] = command
        # get corresponding army command
        for convoyed_army_id in commands:
            convoyed_army = commands[convoyed_army_id]
            if convoyed_army.location.is_occupied.type == "army" and convoyed_army.legal == 1 and convoyed_army.origin == command.origin and convoyed_army.destination == command.destination:
                for convoying_command_id in commands:
                    convoying_command = commands[convoying_command_id]
                    if convoying_command.convoy == True and convoying_command.origin == command.origin and convoying_command.destination == command.destination:
                        convoying_commands[convoying_command_id] = convoying_command
                if len(convoying_commands) == 1:
                    if command.location in command.origin.neighbors.values() and command.location in command.destination.neighbors.values():
                        convoyed_army.legal = 1
                    else:
                        convoyed_army.legal = "False - incomplete convoy path"
                else:
                    convoy_path_length = len(convoying_commands)
                    convoy_path_count = 0
                    convoy_location_neighbor_boolean = False
                    convoy_destination_neighbor_boolean = True
                    for each_convoy_id in convoying_commands:
                        convoy_path_count += 1
                        each_convoy = convoying_commands[each_convoy_id]
                        if each_convoy.location in command.location.neighbors.values():
                            convoy_location_neighbor_boolean = True
                        if each_convoy.location in command.destination.neighbors.values():
                            convoy_destination_neighbor_boolean = True
                        for neighboring_convoy_id in convoying_commands:
                            neighboring_convoy = convoying_commands[neighboring_convoy_id]
                            if neighboring_convoy != each_convoy and neighboring_convoy.location in each_convoy.location.neighbors.values():
                                convoyed_army.legal = 1
                            else:
                                convoyed_army.legal = "False - invalid convoy path"
                                break
                        if convoyed_army.legal == False:
                            break
                        else:
                            if convoy_path_count == convoy_path_length:
                                if convoy_location_neighbor_boolean == True and convoy_destination_neighbor_boolean == True:
                                    convoyed_army.legal = True
                                else:
                                    convoyed_army.legal = "False - no neighbor to convoy origin or destination"
                            else:
                                continue
                        if convoyed_army.legal == False:
                            break
                    if convoyed_army.legal == False:
                        break   
            else:
                continue
        return command
                
def filter_convoys(commands):
    for command_id in commands:
        command = commands[command_id]
        if command.legal != 1 and command.convoy == True:
            command = filter_convoyer(command)
    for command_id in commands:
        command = commands[command_id]
        if command.legal != 1:
            command = filter_convoyed_army(command, commands)
    for command_id in commands:
        command = commands[command_id]
        if command.legal != 1:
            command = filter_convoy_support(command, commands)
    for command_id in commands:
        command = commands[command_id]
        if command.legal == 1 and command.convoy == True:
            command = filter_valid_convoy_paths(command, commands)
    for command_id in commands:
        command = commands[command_id]
        if command.legal != 1:
            command.origin = command.location
            command.destination = command.location
    return commands

    
    
