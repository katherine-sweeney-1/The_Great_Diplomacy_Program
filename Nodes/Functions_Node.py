from Class_Node import Node
from Class_Sub_Node import Coastal_Node
from Visualize_Node_Class import GraphVisualization
import sys
#import os
#sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Units"))
sys.path.append("../The_Great_Diplomacy_Program/Units")
from Class_Unit import Unit

# get a dictionary of node data
def get_nodes_data_dictionary(csv_file):
    nodes_data_dictionary = {}
    # parse the csv file
    open_file = open(csv_file)
    i = 0
    for line in open_file.readlines():
        line = line.replace("\n", "")
        line = line.split(sep = ",")
        if i > 0:
            # create a nested dictionary of node information
            nested_entry = {"Full Name": line[1], 
                            "Type": line[2],
                            "Neighbors": line[3],
                            "Country": line[4],
                            "Dot": line[5],
                            "Home SupCenter": line[6]}
            nodes_data_dictionary[line[0]] = nested_entry
        i += 1
    return nodes_data_dictionary

# create node objects
def create_nodes(nodes_data, nodes_data_coastal, nodes_data_fleet_coastal, nodes_data_fleet_special_coastal):
    nodes_noncoastal = {}
    nodes_coastal = {}
    nodes_data_dictionary = get_nodes_data_dictionary(nodes_data)
    coastal_dictionary = get_nodes_data_dictionary(nodes_data_coastal)
    fleet_coastal_dictionary = get_nodes_data_dictionary(nodes_data_fleet_coastal)
    fleet_special_coastal_dictionary = get_nodes_data_dictionary(nodes_data_fleet_special_coastal)
    # create nodes for non-coastal territories
    for node_data_id in nodes_data_dictionary:
        node = Node(node_data_id, nodes_data_dictionary[node_data_id])
        nodes_noncoastal[node_data_id] = node
    # create nodes for coastal territories
    for coastal_data_id in coastal_dictionary:
        node = Coastal_Node(coastal_data_id, coastal_dictionary[coastal_data_id])
        parent_name = node.name[:3]
        parent_node = nodes_noncoastal[parent_name]
        node.assign_parent(parent_node)
        nodes_coastal[coastal_data_id] = node
    # coastal nodes assign sibling nodes
    for coastal_id in nodes_coastal:
        for coastal_id in nodes_coastal:
            nodes_coastal[coastal_id].assign_sibling(nodes_coastal)
    # combine non-coastal and coastal nodes
    nodes = {**nodes_noncoastal, **nodes_coastal}
    # assign class properties to nodes
    for node_id in nodes:
        if "-" in node_id:
            node_data_dictionary = coastal_dictionary #get_nodes_data_dictionary(nodes_data_coastal)
            fleet_neighbors_string = fleet_special_coastal_dictionary[node_id]["Neighbors"]

        else:
            node_data_dictionary = nodes_data_dictionary  #get_nodes_data_dictionary(nodes_data)
            if nodes[node_id].node_type == "Coast":
                fleet_neighbors_string = fleet_coastal_dictionary[node_id]["Neighbors"]
        neighbors_string = node_data_dictionary[node_id]["Neighbors"]
        dots_string = node_data_dictionary[node_id]["Dot"]
        homesupplycenter_string = node_data_dictionary[node_id]["Home SupCenter"]
        neighbors_string = neighbors_string.split(" ")
        # assign string data to node class properties
        nodes[node_id].assign_neighbors(nodes, neighbors_string)
        nodes[node_id].assign_dot(dots_string)
        nodes[node_id].assign_supply_center(homesupplycenter_string)
        # Assign coastal fleet neighbors (because fleets can only move along coasts or into seas)
        if nodes[node_id].node_type == "Coast":
            fleet_neighbors_string = fleet_neighbors_string.split(" ")
            nodes[node_id].assign_fleet_neighbors(nodes, fleet_neighbors_string)
            """
            if "-" in node_id:
                nodes[node_id].assign_fleet_neighbors(nodes, fleet_neighbors_string)
            else:
                #fleet_neighbors_string = fleet_coastal_dictionary[node_id]["Neighbors"]
                fleet_neighbors_string = fleet_neighbors_string.split(" ")
                nodes[node_id].assign_fleet_neighbors(nodes, fleet_neighbors_string)
            """
    return nodes

"""
# Coastal nodes occupied status
def assign_occ_coastal(nodes):
    for node_id in nodes:
        if isinstance (nodes[node_id], Coastal_Node):
            parent_occ = False
            if isinstance(nodes[node_id].is_occupied, Unit):
                node = nodes[each_id[:3]]
                print("check 0", node.name)
                nodes[node_id].assign_occ_to_family(parent_occ, node)
        elif len(node_id[:3]) > 0:
            if isinstance(nodes[node_id].is_occupied, Unit):
                parent_occ = True
                for each_id in nodes:
                    if each_id[:3] in node_id and each_id != node_id:
                        node = nodes[each_id[:3]]
                        print("check", each_id, node_id, node.name)
                        nodes[each_id].assign_occ_to_family(parent_occ, node)
                        #nodes[node].assign_parent_status(node)
    return nodes
"""

# Coastal nodes occupied status
def assign_occ_coastal(nodes):
    for node_id in nodes:
        if isinstance (nodes[node_id], Coastal_Node):
            parent_occupied = False
            if isinstance(nodes[node_id].is_occupied, Unit):
                parent_node = nodes[node_id[:3]]
                parent_occupied = True
                #nodes[node_id].assign_occ_to_family(parent_occupied, parent_node)
                occupying_unit = nodes[node_id].is_occupied
                nodes[node_id].assign_occ_to_family(parent_occupied, parent_node, occupying_unit)
                parent_node.assign_parent_status(occupying_unit)
    return nodes

# Nodes occupied status
def assign_occupied(nodes, units):
    for node_id in nodes:
        nodes[node_id].assign_occupied(False)
    for unit_id in units:
        #print("checking,", unit_id)
        occupied_node = units[unit_id].location
        occupied_node.assign_occupied(units[unit_id])
        #print("Is occupied inside nodes function?", occupied_node.is_occupied)
    return nodes, units

def create_graph (nodes):
    territory_graph = GraphVisualization()
    for node_id in nodes:
        neighbors = nodes[node_id].neighbors.split(" ")
        for neighbor in neighbors:
            territory_graph.addEdge(node_id, neighbor)
    return territory_graph

def run_create_graph (nodes):
    visual_graph = create_graph(nodes)
    visual_graph.visualize()
    return visual_graph