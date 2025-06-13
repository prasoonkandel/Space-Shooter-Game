# run this file to play game

import pygame
from Objects.spaceship import Spaceship
from Objects.bullet import Bullet
from Objects.enemy import Enemy, create_new_enemy
create_new_bullet = Bullet.create_new_bullet

clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.font.init()
# Constants
WIDTH, HEIGHT = 540, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
# loading sounds
fire_sound = pygame.mixer.Sound("assets/Sounds/fire.mp3")
pygame.mixer.music.load("assets/Sounds/background.wav")
pygame.mixer.music.play(-1)
# loding images
bullet_image = pygame.image.load("assets/Images/bullet.png")
space_ship_image = pygame.image.load("assets/Images/ship.png")
stars_image = pygame.image.load("assets/Images/stars.png")
enemy_img = pygame.image.load("assets/Images/enemy.png")

space_ship = Spaceship(space_ship_image, WIDTH//2, HEIGHT-100, 0.2)

fire_delay = 100
last_fired = 0
last_enemy_spawned = 0
running = True
while running:
    clock.tick(60)
    pygame.display.set_caption(f"Space Shooter - FPS: {clock.get_fps():.2f}")
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                space_ship.fire(bullet_image, fire_sound)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        space_ship.move_left(SCREEN)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        space_ship.move_right(SCREEN)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        space_ship.move_up(SCREEN)

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        space_ship.move_down(SCREEN)
    space_key_pressed = keys[pygame.K_SPACE]
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - last_fired >= fire_delay:
        space_ship.fire(bullet_image, fire_sound)
        last_fired = current_time
    if pygame.time.get_ticks() - last_enemy_spawned >= 250:
        create_new_enemy(enemy_img, SCREEN_WIDTH=WIDTH)

        last_enemy_spawned = pygame.time.get_ticks()
    Enemy.show(SCREEN)
    Bullet.show_bullets(SCREEN)
    space_ship.show(SCREEN)

    pygame.display.flip()

    space_ship.show(SCREEN)
    pygame.display.flip()
pygame.quit()
