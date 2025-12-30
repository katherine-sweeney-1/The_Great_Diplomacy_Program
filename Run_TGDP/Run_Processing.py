import sys
import os
#sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
sys.path.append("../The_Great_Diplomacy_Program/Process_Moves")
from Functions_Support import get_success_supports
from Functions_Attack import get_success_attacks
from Functions_Post_Outcome import process_outcomes
#sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_commands
from Functions_Convoy import filter_convoys

# need to include filter owners I think 
# do this later 
def run_processing(commands, commanders, nodes, units):
    valid_commands, invalid_commands = filter_commands(commands, commanders)
    valid_commands = filter_convoys(valid_commands)
    valid_commands = get_success_supports(valid_commands)
    valid_commands = get_success_attacks(valid_commands)
    nodes, units = process_outcomes(valid_commands, nodes, units)
    return nodes, units, valid_commands


