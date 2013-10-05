import pygame 
class Bomb(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('BombSpriteSheet.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 25, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.fuse_states = { 0: (0, 0, 25, 30), 1: (25, 0, 25, 30)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'bomb':
            self.clip(self.fuse_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self.update('bomb')