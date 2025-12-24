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
    #valid_commands = filter_convoys(valid_commands)
    valid_commands = get_success_supports(valid_commands)
    valid_commands = get_success_attacks(valid_commands)
    #for valid in valid_commands:
    #    print(valid, valid_commands[valid].succeed, valid_commands[valid].predet_outcome)
    for command_id in commands:
        #print(command_id, commands[command_id].succeed, commands[command_id].predet_outcome)
        if commands[command_id].succeed == commands[command_id].predet_outcome and commands[command_id].legal == 1:
           print(command_id, "Correct outcome", commands[command_id].succeed)
        else:
            print("uh oh", command_id, commands[command_id].strength, commands[command_id].legal, commands[command_id].succeed)
        """
        if commands[id].check_other_attacks == True:
            if commands[id].succeed == commands[id].predet_outcome and commands[id].legal == 1:
                print(id, "Correct outcome", commands[id].succeed)
            else:
                print("uh oh", id, commands[id].strength, commands[id].legal, commands[id].succeed)
        """
    nodes, units = process_outcomes(valid_commands, nodes, units)
    return nodes, units, valid_commands


