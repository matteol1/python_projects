import pygame
import sys
import time
import numpy as np
import life as life

TIME = 10
GRID_SIZE = 5

pygame.init()
size = width, height = 600, 500

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

game_on = 0
game_over = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if game_on == 0 and game_over==False:

        # Draw title
        title = largeFont.render("Play the Game of Life", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playButton = pygame.Rect((width / 2 - width/8), (height / 2), width / 4, 50)
        play = mediumFont.render("Play", True, black)
        playRect = play.get_rect()
        playRect.center = playButton.center
        pygame.draw.rect(screen, white, playButton)
        screen.blit(play, playRect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playButton.collidepoint(mouse):
                time.sleep(0.2)
                game_on = 1

    else:

        grid = life.init_grid(GRID_SIZE)
        #boat is stationary
        #grid = np.array([
        #    [0,0,0,0,0],
        #    [0,1,1,0,0],
        #    [0,1,0,1,0],
        #    [0,0,1,0,0],
        #    [0,0,0,0,0]]
        #)

        # Draw game board
        tile_size = (2/3)*width/GRID_SIZE
        tile_origin = ( (width - tile_size*GRID_SIZE)/2 ,
                       height / 8 + 20)
        tiles = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                if grid[i][j] == 1:
                    pygame.draw.rect(screen, green, rect, 0)
                else:
                    pygame.draw.rect(screen, black, rect, 0)

                
                row.append(rect)
            tiles.append(row)

        if game_over == False:
            game_over = life.terminal(grid, GRID_SIZE)
            
            grid = life.evolve(grid, GRID_SIZE)

        # Show title
        if game_over:
            game_on = 0
            title = f"Life ended"
            time.sleep(2)
        else:
            title = f"Evolving..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        if game_over == True and game_on == 0 :
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    game_on=1
                    game_over = False

        time.sleep(0.3)

    pygame.display.flip()
