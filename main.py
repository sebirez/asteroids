import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from circleshape import *
import sys



def main():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y, 0)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:                                                             #initiate game loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    if player.cooldown <= 0:
                        player.shoot()
                        player.cooldown = PLAYER_SHOOT_COOLDOWN
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))                              #draw black screen                              
        updatable.update(dt)
        for asteroid in asteroids:
            collision = asteroid.collision_check(player)
            if collision:
                print("Game over!")
                sys.exit()
            for shot in shots:
                hit = asteroid.collision_check(shot)
                if hit:
                    shot.kill()
                    asteroid.split()

            

        for d in drawable:
            d.draw(screen)                                        
        
        pygame.display.flip()                                               #render screen and player
        ms_next_frame = game_clock.tick(60)
        dt = ms_next_frame/1000
    
    
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
        main()