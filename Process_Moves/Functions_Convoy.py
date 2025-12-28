import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

# filter units that convoy
# command filter != 1 because convoys will get flared in previous filters 
def filter_convoyer(command):
    # Convoy must have a different origin, location, and destination
    if command.location != command.origin and command.location != command.destination and command.origin != command.destination and command.unit.type == "fleet":
        # Unit convoying is a fleet and unit being convoyed is an army
        if command.origin.is_occupied.type == "army":
            if command.origin.node_type == "Coast" and command.destination.node_type == "Coast":
                if command.location.node_type == "Sea":
                    # might need to move to the convoy path function
                    # issue here with double convoys
                    """
                    if command.location in command.origin.neighbors.values() or command.destination in command.origin.neighbors.values():
                        command.legal = 1
                    else:
                        command.legal = "False - convoy is not neighbors with convoying unit"
                    """
                    command.legal = 1
                else:
                    command.legal = "False - convoy location is not a sea"
            else:
                command.legal = "False - convoy is not between coasts"
        else:
            command.legal = "False - convoyed unit is not an army"
    else:
        command.legal = command.legal
    return command

def filter_convoyed_army (command, commands):
    if command.location == command.origin and command.origin != command.destination and command.unit.type == "army":
        for convoyer_command_id in commands:
            convoyer_command = commands[convoyer_command_id]
            #print(command.unit.id, command.origin.name, command.destination.name)
            #print(convoyer_command.unit.id, convoyer_command.origin.name, convoyer_command.destination.name)
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





"""

need to consider double convoys when either

    convoy is neighbors with location and not destination

    convoy is neighbors with destination and not location

"""
def filter_valid_convoy_paths(command, commands):
        convoying_commands = {}
        convoying_commands[command.unit.id] = command
        for convoying_command_id in commands:
            convoying_command = commands[convoying_command_id]
            if convoying_command.convoy == True and convoying_command.origin == command.origin and convoying_command.destination == command.destination:
                convoying_commands[convoying_command_id] = convoying_command
        if len(convoying_commands) == 1:
            if command.location in command.origin.neighbors.values() and command.location in command.destination.neighbors.values():
                command.legal = 1
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
                        command.legal = 1
                    else:
                        command.legal = "False - invalid convoy path"
                        break
                if command.legal == False:
                    break
                else:
                    if convoy_path_count == convoy_path_length:
                        if convoy_location_neighbor_boolean == True and convoy_destination_neighbor_boolean == True:
                            command.legal = True
                        else:
                            command.legal = "False - no neighbor to convoy origin or destination"
                    else:
                        continue
        return command
                

    

def filter_convoys(commands):
    """
    for command_id in commands:
        command = commands[command_id]
        if command.convoy == True:
            print("convoying unit", command.unit.id)
    """
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

    
    
