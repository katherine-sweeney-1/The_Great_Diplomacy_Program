class Command ():

    def __init__ (self, country_string):
        self.country = country_string
        self.legal = 1
        self.strength = 1
        self.check_other_attacks = False
        self.original_support_origin = False
        self.original_support_destination = False
        self.original_coastal_location = False

    def assign_commander(self, cmding_owner, commanders):
        self.human = commanders[cmding_owner]
        return self.human
    
    def assign_unit(self, unit_string, units):
        if unit_string in units:
            self.unit = units[unit_string]
        else:
            self.legal = 0
            self.unit = 0
        return self.unit
    
    def assign_location(self, loc_string, nodes):
        self.location = nodes[loc_string]
        return self.location
    
    def assign_origin (self, origin_string, nodes):
        self.origin = nodes[origin_string]
        return self.origin
    
    def assign_destination (self, dest_string, nodes):
        self.destination = nodes[dest_string]
        return self.destination
    
    def legal_command (self, filter_value):
        self.legal = filter_value
    
    def cmd_strength(self, additional_strength):
        self.strength = self.strength + additional_strength
        return self.strength
    
    def success(self, cmd_valid_boolean):
        self.succeed = cmd_valid_boolean
        return self.succeed
    
    def retreat_boolean(self, possible_retreat):
        self.retreat = possible_retreat
        return self.retreat
    
    def assign_outcome_location(self, node):
        self.outcome_location = node
        return self.outcome_location
    
    def predetermined_outcome(self, predet_outcome):
        self.predet_outcome = predet_outcome
        return self.predet_outcome

    def checking_other_attacks(self, check_other_attacks_boolean):
        self.check_other_attacks = check_other_attacks_boolean
        return self.check_other_attacks

    def convoy_status (self, convoy_boolean):
        self.convoy = convoy_boolean
        return self.convoy
 
    def assign_original_coastal_location(self, original_coastal_location_node):
        self.original_coastal_location = original_coastal_location_node
        return self.original_coastal_location
    
    def assign_original_support_origin (self, original_support_origin_node):
        self.original_support_origin = original_support_origin_node
        return self.original_support_origin
    
    def assign_original_support_destination (self, original_support_destination_node):
        self.original_support_destination = original_support_destination_node
        return self.original_support_destination
    
    def assign_retreat_disband(self, retreat_boolean):
        self.needs_retreat = retreat_boolean
        return self.needs_retreat
    
    def assign_retreat_nodes(self, retreat_options):
        self.retreat_nodes = retreat_options
        return self.retreat_nodes
    
    def assign_displacing_attack(self, displacing_command):
        self.displacing_attack = displacing_command
        return self.displacing_attack
    
    def assign_winter_location (self, winter_location_node):
        self.winter_location = winter_location_node
        return self.winter_location
    
    def print_statement(self):
        print("command for unit {}, country {} has commander {}".format(self.unit.id, self.country, self.human.human))
        print("loc: {}, origin: {}, dest: {}".format(self.loc.name, self.origin.name, self.destination.name))

