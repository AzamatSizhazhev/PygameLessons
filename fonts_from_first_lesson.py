import pygame


def show_text(font, fontname, position):
    font_color = (50, 50, 50)
    text = font.render(f'Hello, pygame! ({fontname})', 1, font_color)
    screen.blit(text, position)


def fonts_demo():
    screen.fill((200, 200, 200))
    font_size = 24
    font = pygame.font.Font(None, font_size)
    show_text(font, 'default', (40, 40))

    print(pygame.font.get_fonts())
    font_names = ['Arial']


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    fonts_demo()

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
