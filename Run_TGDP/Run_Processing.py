import sys
sys.path.append("../The_Great_Diplomacy_Program/Process_Moves")
from Functions_Support import get_success_supports
from Functions_Attack import get_success_attacks
from Functions_Post_Outcome import process_outcomes
from Functions_Filter import filter_commands
from Functions_Convoy import filter_convoys

def run_processing(commands, commanders, nodes, units):
    commands = filter_commands(commands, commanders)
    commands = filter_convoys(commands)
    commands = get_success_supports(commands)
    commands = get_success_attacks(commands)
    nodes, units = process_outcomes(commands, nodes, units)
    return nodes, units, commands


