# / OBJECTS
import pygame
# // entity builder
class Entity:

    def __init__(self, name, entity_z_init, entity_z_count, entity_w_init, entity_w_count, state, esc_possible):
        self.name = name
        self.entity_z_init = entity_z_init
        self.entity_z_count = entity_z_count
        self.entity_w_init = entity_w_init
        self.entity_w_count = entity_w_count
        self.state = state
        self.esc_possible = esc_possible

    # /// attack action
    def attack(self):
        print(f"{self.name} atakuje!")

    # /// die action
    def die(self):
        print(f"{self.name} został zabity!")
        self.state = False

# // door builder
class Door:
    def __init__(self, door_id, door_state, visit_in_turn):
        self.door_ID = door_id
        self.door_state = door_state
        self.visit_in_turn = visit_in_turn

        def open():
            self.door_state = True

        def close():
            self.door_state = False

# // room builder
class Room:
    def __init__(self, room_id, visit_in_turn):
        self.room_id = room_id
        self.visit_in_turn = visit_in_turn

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        # get mouse possition
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditios
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
