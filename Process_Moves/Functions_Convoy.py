import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

# filter units that convoy
# command filter != 1 because convoys will get flared in previous filters 
def filter_convoyer(command):
    # Convoy must have a different origin, location, and destination
    #print(command.unit.id, command.unit.type)
    #print(command.location.name, command.origin.name, command.destination.name)
    if command.location != command.origin and command.location != command.destination and command.origin != command.destination and command.legal != 1 and command.unit.type == "fleet":
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

        # Unit being convoyed is an army
        """
        if command.origin.is_occupied.type == "Army":
            command.legal = 1
        else:
            command.legal = "False - convoyed unit is not an army"
        
        # Convoy is between coasts
        if command.origin.node_type == "Coast" and command.destination.node_type == "Coast":
            command.legal = 1
        else:
            command.legal = "False - convoy is not between coasts"
        
        # Convoy location is a sea
        if command.location == "Sea":
            command.legal = 1
        else:
            command.legal = "False - convoy location is not a sea"
        
        # Convoy location and origin are neighbors
        if command.location in command.origin.neighbors.values():
            command.legal = 1
        else:
            command.legal = "False - convoy location and origin are not neighbors"
        """
    else:
        command.legal = command.legal
    print("Convoyer fleet check", command.unit.id, command.legal)
    return command

def filter_convoyed_army (command, commands):
    #print(command.unit.id)
    #print("check", command.location.name, command.origin.name, command.destination.name)
    if command.location == command.origin and command.origin != command.destination and command.legal != 1 and command.unit.type == "army":
        for convoyer_command_id in commands:
            convoyer_command = commands[convoyer_command_id]
            if command.origin == convoyer_command.origin and command.destination == convoyer_command.destination:
                if convoyer_command.legal == convoyer_command.legal:
                    command.legal = 1
                    break
                else:
                    command.legal = "False - convoyed army does not have a legally supporting convoy"
            else:
                command.legal = "False - convoyed army does not have a corresponding convoy"
    else:
        command.legal = command.legal
    print("convoyed army check", command.unit.id, command.legal)
    return command
"""

need to consider double convoys when either

    convoy is neighbors with location and not destination

    convoy is neighbors with destination and not location

"""
def filter_valid_convoy_paths(command, commands):
        # Convoy connects a path between coasts
        for neighbor_id in command.origin.neighbors():
            #not sure if this is correct
            if command.destination in command.origin.neighbors.values() and command.location in command.origin.neighbors.values():
                command.legal = True
            else:
                count = 0
                for convoyer_command_id in commands:
                    convoyer_command = commands[convoyer_command_id]
                    convoyer_command = filter_convoyer(convoyer_command)
                    if command.legal == 1:
                        # n + 1 convoying unit must be neighbors with original convoy
                        if convoyer_command.location in command.location.neighbors.values():
                            # n + 1 convoying unit ends if other command is neighbors with destination
                            if convoyer_command.location in command.destination.neighbors.values():
                                convoy_boolean = True
                            else:
                                count = 0
                                convoyer_command_neighbors_count = len(convoyer_command.location.neighbors)
                                for other_convoyer_neighbor_id in convoyer_command.location.neighbors():
                                    return True
                                #count += 1


def filter_convoys(commands):
    for command_id in commands:
        command = commands[command_id]
        if command.legal == 1:
            continue
        else:
            command = filter_convoyer(command)
        if command.legal == 1:
            continue
        else:
            command = filter_convoyed_army(command, commands)
            if command.legal != 1:
                command.origin = command.location
                command.destination = command.location
    return commands

    
    
