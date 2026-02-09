import sys
sys.path.append("../The_Great_Diplomacy_Program/Nodes")
from Functions_Node import create_nodes
from Functions_Node import assign_occupied
from Functions_Node import assign_occ_coastal
#sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commanders"))
sys.path.append("../The_Great_Diplomacy_Program/Commanders")
from Functions_Commander import create_commanders
from Functions_Commander import update_commanders
#sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commands"))
sys.path.append("../The_Great_Diplomacy_Program/Commands")
from Functions_Command import create_commands

# Create Objects
def create_objects(nodes_data, nodes_data_coastal, nodes_data_fleet_coastal, nodes_data_fleet_special_coastal, commanders_data, units_data, commands_data):
    commanders = create_commanders(commanders_data)
    nodes = create_nodes(nodes_data, nodes_data_coastal, nodes_data_fleet_coastal, nodes_data_fleet_special_coastal)
    commanders, units = update_commanders(commanders, nodes, commanders_data, units_data)
    nodes, units = assign_occupied(nodes, units)
    nodes = assign_occ_coastal(nodes)
    commands = create_commands(commands_data, commanders, nodes, units)
    return commands, commanders, nodes, units