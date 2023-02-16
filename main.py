from random import randint
import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, (255, 255, 255), (
                    self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size, self.cell_size), 1)
                if self.board[i][j] == 10:
                    pygame.draw.rect(surface, (255, 0, 0), (
                        self.left + self.cell_size * j + 1, self.top + self.cell_size * i + 1,
                        self.cell_size - 2, self.cell_size - 2))
                if self.board[i][j] != 10 and self.board[i][j] != -1:
                    font = pygame.font.Font(None, 25)
                    text = font.render(str(self.board[i][j]), True, (100, 255, 100))
                    surface.blit(text, (self.left + self.cell_size * j + 5, self.top + self.cell_size * i))


class Minesweeper(Board):
    def __init__(self, width, height, mines):
        super().__init__(width, height)
        self.mines = mines
        for _ in range(self.mines):
            x, y = randint(0, self.width - 1), randint(0, self.height - 1)
            while self.board[y][x] == 10:
                x, y = randint(0, self.width - 1), randint(0, self.height - 1)
            self.board[y][x] = 10
        self.cash = list()

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * self.width \
                or mouse_pos[1] < self.top or mouse_pos[1] > self.top + self.cell_size * self.height:
            return None
        return (mouse_pos[1] - self.top) // self.cell_size, (mouse_pos[0] - self.left) // self.cell_size

    def get_click(self, mouse_pos):
        start_cell = self.get_cell(mouse_pos)
        if start_cell is not None and self.board[start_cell[0]][start_cell[1]] == -1:
            self.open_cell(start_cell)

    def open_cell(self, mouse_pos):
        row, column = mouse_pos
        right, left, top, down = column + 1, column - 1, row - 1, row + 1
        counter = 0

        if row == 0:
            top = None
        elif row == self.height - 1:
            down = None

        if column == 0:
            left = None
        elif column == self.width - 1:
            right = None

        if right is not None:
            if top is not None and self.board[top][right] == 10:
                counter += 1
            if self.board[row][right] == 10:
                counter += 1
            if down is not None and self.board[down][right] == 10:
                counter += 1
        if left is not None:
            if top is not None and self.board[top][left] == 10:
                counter += 1
            if self.board[row][left] == 10:
                counter += 1
            if down is not None and self.board[down][left] == 10:
                counter += 1
        if top is not None and self.board[top][column] == 10:
            counter += 1
        if down is not None and self.board[down][column] == 10:
            counter += 1

        self.board[row][column] = counter
        self.cash.append((row, column))

        if counter == 0:
            if right is not None:
                if top is not None and (top, right) not in self.cash:
                    self.open_cell((top, right))
                if (row, right) not in self.cash:
                    self.open_cell((row, right))
                if down is not None and (down, right) not in self.cash:
                    self.open_cell((down, right))
            if left is not None:
                if top is not None and (top, left) not in self.cash:
                    self.open_cell((top, left))
                if (row, left) not in self.cash:
                    self.open_cell((row, left))
                if down is not None and (down, left) not in self.cash:
                    self.open_cell((down, left))
            if top is not None and (top, column) not in self.cash:
                self.open_cell((top, column))
            if down is not None and (down, column) not in self.cash:
                self.open_cell((down, column))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((520, 520))

    running = True
    clock = pygame.time.Clock()
    fps = 60
    sweeper = Minesweeper(15, 15, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sweeper.get_click(event.pos)
        screen.fill((0, 0, 0))
        sweeper.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
