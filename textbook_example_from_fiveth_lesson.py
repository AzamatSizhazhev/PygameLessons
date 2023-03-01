import os
import pygame
import sys
import random

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image('boom.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


# image = load_image('patrick.png')
# image1 = pygame.transform.scale(image, (200, 100))
# image2 = pygame.transform.scale(image, (100, 200))
#
# screen.fill((255, 255, 255))
# screen.blit(image1, (10, 10))
# screen.blit(image2, (50, 50))
# screen.blit(image, (100, 100))

# all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# sprite.image = load_image('bomb.png')
# sprite.rect = sprite.image.get_rect()
# all_sprites.add(sprite)
#
# sprite.rect.x = 5
# sprite.rect.y = 20
#
# screen.fill((255, 255, 255))
# all_sprites.draw(screen)

# bomb_image = load_image("bomb.png")
# all_sprites = pygame.sprite.Group()
#
# for i in range(50):
#     bomb = pygame.sprite.Sprite(all_sprites)
#     bomb.image = bomb_image
#     bomb.rect = bomb.image.get_rect()
#
#     bomb.rect.x = random.randrange(width)
#     bomb.rect.y = random.randrange(height)

all_sprites = pygame.sprite.Group()
for _ in range(50):
    Bomb(all_sprites)

running = True
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
