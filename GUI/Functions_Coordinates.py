import sys
sys.path.append("../The_Great_Diplomacy_Program/Nodes")
from Functions_Node import get_nodes_data_dictionary
import sys

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"
data_fleet_special_coastal = "data/Data_Ter_Fleet_Special_Coasts.csv"

territory_coordinates = "GUI/Territory_Main_Coordinates.txt"
territory_neighbor_coordinates = "GUI/Territory_Main_and_Neighbors_Coordinates.csv"

nodes_data_main = get_nodes_data_dictionary(data_nodes)
territory_coordinates_file = open(territory_coordinates)
territory_coordinates_file.read()

def get_territories_with_neighbors_coordinates(nodes_data_main, territory_coordinates, territory_neighbor_coordinates):
    # each entry in the nodes dictionary
    territories_neighbors_with_coordinates = {}
    for node_entry in nodes_data_main:
        neighbors = nodes_data_main[node_entry]["Neighbors"]
        neighbors = neighbors.split(" ")
        # get the coordinates for each neighbor for each entry in the nodes dictionary
        neighbors_coordinates = {}
        for neighbor in neighbors:
            with open(territory_coordinates, "r") as file_input, open(territory_neighbor_coordinates, "a") as file_output:
                for line in file_input:
                    if line[0:3] == neighbor:
                        coordinate_tuple = line[4:-1]
                        #print(line[0:3], "rest of line", line[4:-1])
                        neighbors_coordinates[line[0:3]] = coordinate_tuple
        territories_neighbors_with_coordinates[node_entry] = neighbors_coordinates
        with open(territory_neighbor_coordinates, "a") as file_output:
            print(node_entry, territories_neighbors_with_coordinates[node_entry], file = file_output)
    return territories_neighbors_with_coordinates

def assign_coordinates_to_nodes(nodes, coordinate_file, coastal_coordinate_file):
    for node_id in nodes:
        node = nodes[node_id]
        with open (coordinate_file, "r") as file_input:
            for line in file_input:
                if line[0:3] == node_id:
                    coordinates = line[4:-1]
                    coordinates = coordinates.split(" ")
                    x_coordinate = coordinates[0][1:-1]
                    x_coordinate = int(x_coordinate)
                    y_coordinate = coordinates[1][:-1]
                    y_coordinate = int(y_coordinate)
                    coordinates = (x_coordinate, y_coordinate)
                    node.assign_coordinates(coordinates) 
    for coastal_id in nodes:
        node = nodes[coastal_id]
        with  open (coastal_coordinate_file, "r") as file_input:
            for line in file_input:
                if line[0:6] == node_id:
                    coordinates = line[7:-1]
                    coordinates = coordinates.split(" ")
                    x_coordinate = coordinates[0][1:-1]
                    x_coordinate = int(x_coordinate)
                    y_coordinate = coordinates[1][:-1]
                    y_coordinate = int(y_coordinate)
                    coordinates = (x_coordinate, y_coordinate)
                    node.assign_coordinates(coordinates)  
    for node_id in nodes:
        print(node_id, node.coordinate)   
    return nodes

