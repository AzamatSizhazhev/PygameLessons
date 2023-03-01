# import random
# import pygame
#
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
#
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, group, radius, x, y):
#         super().__init__(group)
#         self.image = pygame.Surface((2 * radius, 2 * radius),
#                                     pygame.SRCALPHA, 32)
#         pygame.draw.circle(self.image, pygame.Color("red"),
#                            (radius, radius), radius)
#         self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
#         self.vx = random.randint(-5, 5)
#         self.vy = random.randrange(-5, 5)
#
#     def update(self):
#         self.rect = self.rect.move(self.vx, self.vy)
#         if pygame.sprite.spritecollideany(self, horizontal_borders):
#             self.vy = -self.vy
#         if pygame.sprite.spritecollideany(self, vertical_borders):
#             self.vx = -self.vx
#
#
# class Border(pygame.sprite.Sprite):
#     def __init__(self, x1, y1, x2, y2):
#         super().__init__(all_sprites)
#         if x1 == x2:  # вертикальная стенка
#             self.add(vertical_borders)
#             self.image = pygame.Surface([1, y2 - y1])
#             self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
#         else:  # горизонтальная стенка
#             self.add(horizontal_borders)
#             self.image = pygame.Surface([x2 - x1, 1])
#             self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
#
#
# horizontal_borders = pygame.sprite.Group()
# vertical_borders = pygame.sprite.Group()
#
# all_sprites = pygame.sprite.Group()
# Border(5, 5, width - 5, 5)
# Border(5, height - 5, width - 5, height - 5)
# Border(5, 5, 5, height - 5)
# Border(width - 5, 5, width - 5, height - 5)
#
# for i in range(10):
#     Ball(all_sprites, 20, 100, 100)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill(pygame.Color("white"))
#     all_sprites.update()
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     clock.tick(50)
# pygame.quit()


import pygame


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load("data/mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 500


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("data/pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, m):
            self.rect = self.rect.move(0, 1)


pygame.init()
screen = pygame.display.set_mode((789, 500))
all_sprites = pygame.sprite.Group()
pt = pygame.sprite.Group()
m = Mountain()
all_sprites.add(m)
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pt.add(Landing(event.pos))

    screen.fill(pygame.Color('white'))
    for i in pt:
        i.update()
    all_sprites.draw(screen)
    pt.draw(screen)
    pygame.display.flip()

pygame.quit()
