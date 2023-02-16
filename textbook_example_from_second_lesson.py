import pygame

# К примеру 2
# from random import randint
# def draw():
#     for _ in range(15000):
#         screen.fill((255, 255, 255), (randint(0, width), randint(0, height), 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    # pygame.display.set_caption('Движущийся круг 1')
    # running = True
    # x_pos = 0
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     screen.fill((0, 0, 0))
    #     pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
    #     x_pos += 1
    #     pygame.display.flip()
    # pygame.quit()

    # pygame.display.set_caption('Ненастроенный телевизор')
    # running = True
    # while running:
    #     screen.fill((0, 0, 0))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     draw()
    #     pygame.display.flip()
    # pygame.quit()

    # pygame.display.set_caption('Движущийся круг 2')
    # running = True
    # x_pos = 0
    # v = 20  # пикселей в секунду
    # fps = 60
    # clock = pygame.time.Clock()
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     screen.fill((0, 0, 0))
    #     pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    #     # x_pos += v * clock.tick() / 1000  # v * t в секундах Вариант 1
    #     x_pos += v / fps  # Вариант 2
    #     clock.tick(fps)
    #     pygame.display.flip()
    # pygame.quit()

    # pygame.display.set_caption('Синий круг')
    # running = True
    # clock = pygame.time.Clock()
    # while running:
    #     screen.fill((0, 0, 0))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEMOTION:
    #             pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
    #     pygame.display.flip()
    #     clock.tick(50)

    # pygame.display.set_caption('Мое событие')
    # MYEVENTTYPE = pygame.USEREVENT + 1
    # pygame.time.set_timer(MYEVENTTYPE, 10)
    # # pygame.time.set_timer(MYEVENTTYPE, 0)  # Если надо отменить
    # fps = 50  # количество кадров в секунду
    # clock = pygame.time.Clock()
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == MYEVENTTYPE:
    #             print("Мое событие сработало")
    #     pygame.display.flip()
    #     clock.tick(fps)

    # pygame.display.set_caption('Графический редактор v0.0000001')
    # running = True
    # screen.fill((0, 0, 0))
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEMOTION:
    #             pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
    #     pygame.display.flip()

    # pygame.display.set_caption('Графический редактор v0.0000002')
    # running = True
    # screen2 = pygame.Surface(screen.get_size())
    # x1, y1, w, h = 0, 0, 0, 0
    # drawing = False  # режим рисования выключен
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             drawing = True  # включаем режим рисования
    #             # запоминаем координаты одного угла
    #             x1, y1 = event.pos
    #         if event.type == pygame.MOUSEBUTTONUP:
    #             # сохраняем нарисованное (на втором холсте)
    #             screen2.blit(screen, (0, 0))
    #             drawing = False
    #             x1, y1, w, h = 0, 0, 0, 0
    #         if event.type == pygame.MOUSEMOTION:
    #             # запоминаем текущие размеры
    #             if drawing:
    #                 w, h = event.pos[0] - x1, event.pos[1] - y1
    #     # рисуем на экране сохранённое на втором холсте
    #     screen.fill(pygame.Color('black'))
    #     screen.blit(screen2, (0, 0))
    #     if drawing:  # и, если надо, текущий прямоугольник
    #         if w > 0 and h > 0:
    #             pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    #     pygame.display.flip()


# для обработки событий:
import pygame.examples.eventlist
pygame.examples.eventlist.main()
