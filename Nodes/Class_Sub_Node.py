from Class_Node import Node

class Coastal_Node (Node):
    
    def __init__ (self, node_name, node_info):
        super().__init__(node_name, node_info)
    
    def assign_parent(self, main_obj):
        self.parent = main_obj
        return self.parent
    
    def assign_sibling(self, coastal_dictionary):
        for coastal_id in coastal_dictionary:
            if self.name[:3] in coastal_id and self.name != coastal_id:
                sibling_name = coastal_id
                break
            else:
                continue
        sibling_node = coastal_dictionary[sibling_name]
        self.sibling = sibling_node
        return self.sibling
    
    def assign_occ_to_family(self, parent_occupied, node, occupying_unit):
        if parent_occupied:
            self.is_occupied = 1
            self.sibling.is_occupied = 1
            self.parent_status = self.assign_parent_status(occupying_unit)
        else:
            self.parent.is_occupied = 1
            self.parent_status = self.assign_parent_status(occupying_unit)
            self.sibling.is_occupied = 1
        return self

    def assign_daughter_occupied(self, occupying_unit):
        self.is_daughter_occupied = occupying_unit
        return self.is_daughter_occupied

    def print_statements(self):
        print("node {} has parent node {} and sibling node {}".format(self.name, self.parent.name, self.sibling.name))
        print("occupied {}, {}, {}".format(self.is_occupied, self.parent.is_occupied, self.sibling.is_occupied))
        print("Territory {} / {}".format(self.name, self.full_name))
        print("dot status: {}, hsc status {},occupied status {}".format(self.dot, self.supply_center, self.is_occupied))
        print("neighbors: {}".format(self.neighbors))
        print(" ")