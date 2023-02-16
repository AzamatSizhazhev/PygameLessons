import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        width = 1
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    width = 1
                elif self.board[i][j] == 1:
                    width = 0
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size, self.cell_size),
                                 width)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * self.width \
                or mouse_pos[1] < self.top or mouse_pos[1] > self.top + self.cell_size * self.height:
            return None
        return (mouse_pos[1] - self.top) // self.cell_size, (mouse_pos[0] - self.left) // self.cell_size

    def on_click(self, cell_coords):
        self.board[cell_coords[0]][cell_coords[1]] = abs(self.board[cell_coords[0]][cell_coords[1]] - 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 400))

    # board = Board(5, 7)
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    clock = pygame.time.Clock()
    fps = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
