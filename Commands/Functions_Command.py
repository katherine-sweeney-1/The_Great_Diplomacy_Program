
from Class_Command import Command

def create_commands(commands_starting_data, commanders, nodes, units):
    cmds_dict = {}
    for each_command in commands_starting_data: 
        command = Command(commands_starting_data[each_command]["country"])
        command.assign_commander(commands_starting_data[each_command]["owner"], commanders)
        command.assign_unit(each_command, units)
        command.assign_location(commands_starting_data[each_command]["location"], nodes)
        command.assign_origin(commands_starting_data[each_command]["origin"], nodes)
        command.assign_destination(commands_starting_data[each_command]["destination"], nodes)
        #command.predetermined_outcome(commands_starting_data[each_command]["outcome"])
        command.convoy_status(commands_starting_data[each_command]["convoy"])
        if command.unit != 0:
            cmds_dict[command.unit.id] = command
    return cmds_dict
    
