MAX_POS = 200

class Satellite:
    def __init__(self, linked_systems, distance, speed, id, router, orbit_type, pos):
        self.linked_systems = linked_systems
        self.distance = distance
        self.speed = speed
        self.orbit_type = orbit_type
        self.id = id
        self.router = router
        self.pos = pos

    def update_pos(self):
        if self.pos < 200:
            self.pos+=self.speed
        else:
            self.pos = 0

    def check_proximity(self, system):
        if self.pos-10 <= system.pos <= self.pos+10:
            return True
        else:
            return False