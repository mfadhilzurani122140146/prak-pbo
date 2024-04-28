import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 1
INNER_LINE_WIDTH = 1 
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

FONT = pygame.font.SysFont('comicsans', 80)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * SQUARE_SIZE
        self.y = row * SQUARE_SIZE
        self.value = None

    def draw(self, win):
        pygame.draw.rect(win, BLACK, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE), 0)
        if self.value == 'X':
            text = FONT.render('X', True, WHITE)
            win.blit(text, (self.x + (SQUARE_SIZE - text.get_width()) // 2, self.y + (SQUARE_SIZE - text.get_height()) // 2))
        elif self.value == 'O':
            text = FONT.render('O', True, WHITE)
            win.blit(text, (self.x + (SQUARE_SIZE - text.get_width()) // 2, self.y + (SQUARE_SIZE - text.get_height()) // 2))

    def draw_lines(self, win):
        pygame.draw.line(win, WHITE, (self.x + INNER_LINE_WIDTH, self.y), (self.x + INNER_LINE_WIDTH, self.y + SQUARE_SIZE), INNER_LINE_WIDTH)
        pygame.draw.line(win, WHITE, (self.x + SQUARE_SIZE - INNER_LINE_WIDTH, self.y), (self.x + SQUARE_SIZE - INNER_LINE_WIDTH, self.y + SQUARE_SIZE), INNER_LINE_WIDTH)
        pygame.draw.line(win, WHITE, (self.x, self.y + INNER_LINE_WIDTH), (self.x + SQUARE_SIZE, self.y + INNER_LINE_WIDTH), INNER_LINE_WIDTH)
        pygame.draw.line(win, WHITE, (self.x, self.y + SQUARE_SIZE - INNER_LINE_WIDTH), (self.x + SQUARE_SIZE, self.y + SQUARE_SIZE - INNER_LINE_WIDTH), INNER_LINE_WIDTH)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def is_empty(self):
        return self.value == None


class Board:
    def __init__(self):
        self.board = [[Square(row, col) for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]

    def draw(self, win):
        for row in self.board:
            for square in row:
                square.draw(win)
                square.draw_lines(win)

    def get_square(self, row, col):
        return self.board[row][col]

    def is_full(self):
        for row in self.board:
            for square in row:
                if square.is_empty():
                    return False
        return True


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    def next_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def make_move(self, row, col):
        square = self.board.get_square(row, col)
        if square.is_empty():
            square.set_value(self.turn)
            self.next_turn()

    def check_winner(self):
        for i in range(BOARD_ROWS):
            if self.board.get_square(i, 0).get_value() == self.board.get_square(i, 1).get_value() == self.board.get_square(i, 2).get_value() != None:
                return self.board.get_square(i, 0).get_value(), [(i, 0), (i, 1), (i, 2)]
            if self.board.get_square(0, i).get_value() == self.board.get_square(1, i).get_value() == self.board.get_square(2, i).get_value() != None:
                return self.board.get_square(0, i).get_value(), [(0, i), (1, i), (2, i)]
        if self.board.get_square(0, 0).get_value() == self.board.get_square(1, 1).get_value() == self.board.get_square(2, 2).get_value() != None:
            return self.board.get_square(0, 0).get_value(), [(0, 0), (1, 1), (2, 2)]
        if self.board.get_square(0, 2).get_value() == self.board.get_square(1, 1).get_value() == self.board.get_square(2, 0).get_value() != None:
            return self.board.get_square(0, 2).get_value(), [(0, 2), (1, 1), (2, 0)]
        return None, None

    def reset(self):
        self.board = Board()
        self.turn = 'X'


def draw_lines():
    pygame.draw.line(win, WHITE, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(win, WHITE, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(win, WHITE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(win, WHITE, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_winner_line(win, winner, start_pos, end_pos):
    pygame.draw.line(win, GREEN, start_pos, end_pos, WIN_LINE_WIDTH)


def draw_winner_message(win, winner):
    if winner:
        text = FONT.render(f'{winner} wins!', True, GREEN)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))


def draw_board(board):
    board.draw(win)


def main():
    run = True
    game = Game()
    winner = None

    while run:
        win.fill(BLACK)
        draw_lines()
        draw_board(game.board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not winner:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if clicked_row < BOARD_ROWS and clicked_col < BOARD_COLS:
                    game.make_move(clicked_row, clicked_col)
                    winner, winning_line = game.check_winner()
                    if winner or game.board.is_full():
                        draw_board(game.board)
                        draw_winner_message(win, winner)
                        if winning_line:
                            start_pos = (winning_line[0][1] * SQUARE_SIZE + SQUARE_SIZE // 2, winning_line[0][0] * SQUARE_SIZE + SQUARE_SIZE // 2)
                            end_pos = (winning_line[2][1] * SQUARE_SIZE + SQUARE_SIZE // 2, winning_line[2][0] * SQUARE_SIZE + SQUARE_SIZE // 2)
                            draw_winner_line(win, winner, start_pos, end_pos)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        game.reset()

        pygame.display.update()
        
            
if __name__ == "__main__":
    main()

