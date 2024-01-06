# // entity builder
class Entity:
    def __init__(self, name, entity_z_count, entity_w_count, state, esc_possible):
        self.name = name
        self.entity_z_init = self.entity_z_count = entity_z_count

        self.entity_w_init = self.entity_w_count = entity_w_count
        self.state = state
        self.esc_possible = esc_possible


# // room builder
class Room:
    def __init__(self, room_num, room_state=False, max_visit_count=9999, visit_count=0):
        self.room_num = room_num
        self.room_state = room_state
        self.max_visit_count = max_visit_count
        self.visit_count = visit_count
