import pygame
import time
from pygame.sprite import Sprite

from Objects.bullet import Bullet
create_new_bullet = Bullet.create_new_bullet


class Spaceship(Sprite):
    speed = 5

    def __init__(self, image, x=0, y=0,  scale=1):
        super().__init__()
        self.image = pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def show(self, screen):
        screen.blit(self.image, (self.rect.x-self.width/2, self.rect.y))

    def move_left(self, screen):
        if self.rect.x <= 0 + self.width/2:
            self.rect.x -= 0
        else:
            self.rect.x -= self.speed

    def move_right(self, screen):

        if self.rect.x >= screen.get_width() - self.width/2:
            self.rect.x += 0
        else:
            self.rect.x += self.speed

    def move_up(self, screen):
        if self.rect.y <= 0:
            self.rect.y -= 0
        else:
            self.rect.y -= self.speed

    def move_down(self, screen):
        if self.rect.y >= screen.get_height() - self.height:
            self.rect.y += 0
        else:
            self.rect.y += self.speed

    def fire(self, bullet_img, fire_sound):
        fire_sound.play()
        create_new_bullet(bullet_img, self.rect.x, self.rect.y)
