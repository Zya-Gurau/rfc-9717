MAX_POS = 200

class Satellite:
    def __init__(self, speed, id, pos):
        self.speed = speed
        self.id = id
        self.pos = pos
        self.linked_systems = []
    
    def add_link(self, system):
        self.linked_systems.append(system)
    def add_links(self,systems):
        self.linked_systems.extend(systems)

    def update_pos(self):
        if self.pos < 200:
            self.pos+=self.speed
        else:
            self.pos = 0

    def check_proximity(self, system):
        if self.pos-30 <= system.pos <= self.pos+30:
            return True
        else:
            return False