import sys
sys.path.append("../The_Great_Diplomacy_Program/Nodes")
from Functions_Node import get_nodes_data_dictionary

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"
data_fleet_special_coastal = "data/Data_Ter_Fleet_Special_Coasts.csv"

"""
dictionary key: name
dictionary value["Neighbors"] = neighbors (need to split by " ")
"""
nodes_data_main = get_nodes_data_dictionary(data_nodes)
for node_entry in nodes_data_main:
    #print(node_entry, nodes_data_main[node_entry]["Neighbors"])
    neighbors = nodes_data_main[node_entry]["Neighbors"]
    print(neighbors)
    


    
