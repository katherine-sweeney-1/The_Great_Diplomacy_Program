import sys
sys.path.append("../The_Great_Diplomacy_Program/Process_Moves")
from Functions_Support import get_success_supports
from Functions_Attack import get_success_attacks
from Functions_Post_Outcome import process_outcomes, get_retreats_from_input
from Functions_Filter import filter_commands
from Functions_Convoy import filter_convoys

def run_processing(commands, commanders, nodes, units):
    commands = filter_commands(commands, commanders)
    commands = filter_convoys(commands)
    commands = get_success_supports(commands)
    commands = get_success_attacks(commands)
    commands = process_outcomes(commands, commanders, nodes, units)
    #commands, processed_commands, nodes, processed_nodes, units, processed_units = process_outcomes(commands, nodes, units)
    #commands, processed_commands, nodes, processed_nodes, units
    #return commands, processed_commands, processed_nodes, processed_units
    return commands


def run_post_processing(commands, commanders, nodes, units):
    commands = get_retreats_from_input(commands)
    #commands, commanders, nodes, units = process_outcomes(commands, commanders, nodes, units)
    return commands, commanders, nodes, units