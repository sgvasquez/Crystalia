import pygame
import Link

               
pygame.init()
 
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Crystalia, la Torre Perdida")
clock = pygame.time.Clock()
player = Link.Link((15, 15))
 
game_over = False
 
while game_over == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    player.handle_event(event)             
    screen.fill(pygame.Color('grey'))  
    screen.blit(player.image, player.rect)
 
    pygame.display.flip()              
    clock.tick(10)
 
pygame.quit ()