import pygame
import Bomb
class Link(pygame.sprite.Sprite):  
    def __init__(self, position):
        self.sheet = pygame.image.load('LinkSpriteSheet.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 44, 47))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (59, 0, 32, 43), 1: (59, 59, 32, 32) }
        self.right_states = { 0: (179, 59, 32, 34), 1: (181, 0, 30, 31) }
        self.up_states = { 0: (123, 0, 26, 40), 1: (123, 59, 26, 34) }
        self.down_states = { 0: (0, 0, 44, 47), 1: (0, 59, 28, 34) }
        self.atkleft_states = { 0: (47, 179, 56, 32), 1: (59, 59, 32, 32)}
        self.atkright_states = { 0: (165, 179, 58, 32), 1: (181, 0, 30, 31)}
        self.atkup_states = { 0: (119, 167, 34, 58), 1: (123, 59, 26, 34)}
        self.atkdown_states = { 0: (0, 167, 34, 56), 1: (0, 59, 28, 34)}
 
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
        
        if direction == 'left':
            self.clip(self.left_states)
            if self.rect.x > 0:
                self.rect.x -= 5 
            else:
                self.rect.x -= 0
        if direction == 'right':
            self.clip(self.right_states)
            if self.rect.x <= 608:
                self.rect.x += 5
            else:
                self.rect.x += 0
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y > 0:
                self.rect.y -= 5
            else:
                self.rect.y -= 0
        if direction == 'down':
            self.clip(self.down_states)
            if self.rect.y <= 438:
                self.rect.y += 5
            else:
                self.rect.y += 0

 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        if direction == 'atkup':
            self.clip(self.atkup_states)
        if direction == 'atkdown':
            self.clip(self.atkdown_states)
        if direction == 'atkleft':
            self.clip(self.atkleft_states)
        if direction == 'atkright':
            self.clip(self.atkright_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 
    def handle_event(self, event):
        k = pygame.key.get_pressed()
        u = k[pygame.K_UP]
        d = k[pygame.K_DOWN]
        l = k[pygame.K_LEFT]
        r = k[pygame.K_RIGHT]
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                self.update('atkdown')
            if event.key == pygame.K_a:
                self.update('atkleft')
            if event.key == pygame.K_d:
                self.update('atkright')
            if event.key == pygame.K_w:
                self.update('atkup')

                    
            if event.key == pygame.K_LEFT:
                self.update('left')
            elif event.key == pygame.K_RIGHT:
                self.update('right')
            elif event.key == pygame.K_UP:
                self.update('up')
            elif event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            elif event.key == pygame.K_RIGHT:
                self.update('stand_right')
            elif event.key == pygame.K_UP:
                self.update('stand_up')
            elif event.key == pygame.K_DOWN:
                self.update('stand_down')
        