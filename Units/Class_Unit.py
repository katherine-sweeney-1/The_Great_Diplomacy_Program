class Unit ():
    
    def __init__ (self, unit_id, unit_type):
        self.id = unit_id
        self.type = unit_type
        self.location = []
        self.command = []

    def assign_location (self, node, location_string, nodes):
        if node:
            self.location = node
        else:
            self.location = nodes[location_string]
        return self.location

    def assign_commander(self, commander):
        self.commander = commander
        return self.commander
    
    def assign_retreat_disband(self, bool):
        self.retreat = bool
        return self.retreat

    def assign_original_location(self, node):
        self.original_location = node
        return self.original_location
    
    def assign_displacing_attack(self, displacing_command):
        self.displacing_attack = displacing_command
        return self.displacing_attack
    def print_statements (self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit command", self.command)