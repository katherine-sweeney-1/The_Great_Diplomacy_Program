class Node ():
    
    def __init__ (self, node_name, node_info):
        self.name = node_name
        self.full_name = node_info["Full Name"]
        self.node_type = node_info["Type"]
        self.is_occupied = False
        self.parent_status = False
        self.fleet_neighbors = False

    def parse_neighbors(self):
        self.neighbors = self.neighbors.split(" ")
        return(self.neighbors)

    def assign_occupied(self, unit):
        self.is_occupied = unit
        return self.is_occupied
    
    def assign_neighbors(self, nodes, neighbors_string):
        neighbors = {}
        for neighbor_data_id in neighbors_string:
            neighbor = nodes[neighbor_data_id]
            neighbors[neighbor_data_id] = neighbor
        self.neighbors = neighbors
        return self.neighbors
    
    def assign_dot(self, dot_string):
        if dot_string == "TRUE":
            self.dot = True
        else:
            self.dot = False
        return self.dot

    def assign_supply_center(self, supply_center_string):
        if supply_center_string != "FALSE":
            self.supply_center = supply_center_string
        else:
            self.supply_center = False
        return self.supply_center
    
    def assign_outcome_occupied(self, unit):
        self.outcome_occupied = unit
        return self.outcome_occupied
    
    def assign_parent_status (self, unit):
        self.parent_status = unit
        return self.parent_status
    
    def assign_fleet_neighbors(self, nodes, fleet_neighbors_string):
        fleet_coastal_neighbors = {}
        for neighbor_data_id in fleet_neighbors_string:
            neighbor = nodes[neighbor_data_id]
            fleet_coastal_neighbors[neighbor_data_id] = neighbor
        self.fleet_neighbors = fleet_coastal_neighbors
        return self.fleet_neighbors

    def assign_coordinates (self, coordinate_tuple):
        self.coordinate = coordinate_tuple
        return self.coordinate
    
    def print_statements (self):
        print("Territory {} / {}".format(self.name, self.full_name))
        print("dot status: {}, hsc status {},occupied status {}".format(self.dot, self.hsc, self.is_occ))
        print("neighbors: {}".format(self.nbrs))
        print("   ")




    
    