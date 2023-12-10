import pygame
import time

pygame.init()
# pygame setup
screen = pygame.display.set_mode((600, 550))
clock = pygame.time.Clock()
running = True
dt = 0

inactive_color = 'yellow'
active_color = 'green'

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2+200, screen.get_height() / 2-200)
pos1 = (300, 150)
pos2 = (200, 300)
pos3 = (400, 300)
pos4 = (200, 450)
pos5 = (400, 450)
centerlink12 = (250,225)
centerlink13 = (350,225)
arrowl12 = (242,210)
arrowr12 = (265,215)
arrowl13 = (335,215)
arrowr13 = (358,210)
centerlink24 = (200,375)
centerlink35 = (400,375)
arrowl24 = (390-200,365)
arrowr24 = (410-200,365)
arrowl35 = (390,365)
arrowr35 = (410,365)
centerarc12 = (220,210)
centerarc13 = (380, 210)
arrowarc12r = (230,220)
arrowarc12l = (210,225)
arrowarc13r = (390,225)
arrowarc13l = (365,220)

active_dict= {0:pos1, 1:pos2, 2:pos3, 3:pos4, 4:pos5}

count = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    active_node = count % 5 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#373737")
    #screen.fill("white")

#    #links
    pygame.draw.line(screen, 'blue', pos1,pos2, 5)
    pygame.draw.line(screen, 'blue', pos1,pos3, 5)
    pygame.draw.line(screen, 'blue', pos2,pos4, 5)
    pygame.draw.line(screen, 'blue', pos3,pos5, 5)
    #arrow heads
    pygame.draw.line(screen, 'blue', centerlink12,arrowl12, 5)
    pygame.draw.line(screen, 'blue', centerlink12,arrowr12, 5)
    pygame.draw.line(screen, 'blue', centerlink13,arrowl13, 5)
    pygame.draw.line(screen, 'blue', centerlink13,arrowr13, 5)
    pygame.draw.line(screen, 'blue', centerlink24,arrowl24, 5)
    pygame.draw.line(screen, 'blue', centerlink24,arrowr24, 5)
    pygame.draw.line(screen, 'blue', centerlink35,arrowr35, 5)
    pygame.draw.line(screen, 'blue', centerlink35,arrowl35, 5)


    rect_arc1 = pygame.Rect(pos1[0]-50, pos1[1], pos3[0]-pos1[0]+50, 2*(pos3[1]-pos1[1]))
    rect_arc2 = pygame.Rect(pos2[0], pos1[1], pos1[0]-pos2[0]+50, 2*(pos3[1]-pos1[1]))
    pygame.draw.arc(screen, 'blue', rect_arc1, 0, 3.14/2, 5) 
    pygame.draw.arc(screen, 'blue', rect_arc2, 3.14/2, 3.14, 5)
    pygame.draw.line(screen, 'blue', centerarc13,arrowarc13l, 5)
    pygame.draw.line(screen, 'blue', centerarc13,arrowarc13r, 5)
    pygame.draw.line(screen, 'blue', centerarc12,arrowarc12l, 5)
    pygame.draw.line(screen, 'blue', centerarc12,arrowarc12r, 5)

    pygame.draw.circle(screen, inactive_color, pos1, 30)
    pygame.draw.circle(screen, inactive_color, pos2, 30)
    pygame.draw.circle(screen, inactive_color, pos3, 30)
    pygame.draw.circle(screen, inactive_color, pos4, 30)
    pygame.draw.circle(screen, inactive_color, pos5, 30)
    
    #redraw active noce
    pygame.draw.circle(screen, active_color, active_dict[active_node], 30)

   # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(0.5) / 1000
    count+=1

pygame.quit()
