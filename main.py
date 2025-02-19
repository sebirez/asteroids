import pygame
from constants import *
from player import *



def main():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    
    while True:                                                             #initiate game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))                              #draw black screen
        player.draw(screen)                                                 #draw player
        player.update(dt)                                                  #rotate left with "a", rotate right with "d"
        
        
        pygame.display.flip()                                               #render screen and player
        ms_next_frame = game_clock.tick(60)
        dt = ms_next_frame/1000
    
    
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
        main()