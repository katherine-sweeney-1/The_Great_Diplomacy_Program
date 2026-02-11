import sys
sys.path.append("../The_Great_Diplomacy_Program/Nodes")
from Functions_Node import get_nodes_data_dictionary

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
#commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"
#data_fleet_special_coastal = "data/Data_Ter_Fleet_Special_Coasts.csv"

territory_coordinates = "GUI/Territory_Main_Coordinates.txt"
territory_neighbor_coordinates = "GUI/Territory_Main_and_Neighbors_Coordinates.csv"

nodes_data_main = get_nodes_data_dictionary(data_nodes)
territory_coordinates_file = open(territory_coordinates)
territory_coordinates_file.read()

coordinates = []
territory_file = "GUI/Data_Main_Names.csv"
coastal_territory_file = "GUI/Data_Coastal_Names.csv"
# coordinates_file = "GUI/Territory_Main_Coordinates.txt"
# coastal_coordinates_file = "GUI/Territory_Coastal_Coordinates.txt"
coordinates_file = "GUI/Europe_Map_Main_Coordinates.txt"
coastal_coordinates_file = "GUI/Europe_Map_Coastal_Coordinates.txt"

# retrieve coordinates for territories
def get_coordinates(click):
    if click:
        x_coordinate = click.x
        y_coordinate = click.y
        coordinate = (x_coordinate, y_coordinate)
        coordinates.append(coordinate)
        write_coordinates_file(coastal_territory_file, coastal_coordinates_file)

# save coordinates for territories in output file
def write_coordinates_file(territory_file, coordinates_file):
    with open(territory_file, "r") as file_input, open(coordinates_file, "a") as file_output:
        count = len(coordinates)
        territory_file_count = 0
        for line in file_input:
            if territory_file_count == count - 1:
                print("current territory is", line)
                print("click the next territory", next(file_input))
                print(line[0:3], coordinates[count - 1], file = file_output)
            territory_file_count += 1
            
def get_territories_with_neighbors_coordinates(nodes_data_main, territory_coordinates, territory_neighbor_coordinates):
    # each entry in the nodes dictionary
    territories_neighbors_with_coordinates = {}
    for node_entry in nodes_data_main:
        print(node_entry)
        neighbors = nodes_data_main[node_entry]["Neighbors"]
        neighbors = neighbors.split(" ")
        # get the coordinates for each neighbor for each entry in the nodes dictionary
        neighbors_coordinates = {}
        for neighbor in neighbors:
            with open(territory_coordinates, "r") as file_input, open(territory_neighbor_coordinates, "a") as file_output:
                for line in file_input:
                    if line[0:3] == neighbor:
                        coordinate_tuple = line[4:-1]
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
        if "-" in coastal_id:
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
        else:
            continue
    return nodes
