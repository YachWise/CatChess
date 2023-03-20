import pygame as pg
import os

from src import ChessEngine

pg.init()

WIDTH = HEIGHT = 800
DIMENSION = 8  # 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "wP",
              "bP"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("assets/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color('white'))
    pg.display.set_caption("Cat Chess @YachWise --v2")
    gamestate = ChessEngine.GameState()
    valid_moves = gamestate.get_valid_moves()
    move_made = False
    load_images()
    running = True
    square_selected = ()  # start with empty square selected
    player_choice = []  # the users start piece location, end piece location

    #  everything in this while loop is while the engine is running
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                column = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if square_selected == (row, column):
                    # clear both choices if user selects same piece/position as their previous clicks
                    square_selected = ()
                    player_choice = []
                else:
                    # if valid click, save the square selected and add it to the player choice tuple arr
                    square_selected = (row, column)
                    player_choice.append(square_selected)

                # user has selected max choices, starting piece and move location
                if len(player_choice) == 2:
                    move = ChessEngine.Move(player_choice[0], player_choice[1], gamestate.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        gamestate.make_move(move)
                        move_made = True
                    square_selected = ()
                    player_choice = []
            # check if user presses a key
            elif event.type == pg.KEYDOWN:
                # if it's a z press, undo the move
                if event.key == pg.K_z:
                    gamestate.undo_move()
                    move_made = True

        if move_made:
            valid_moves = gamestate.get_valid_moves()
            move_made = False

        draw_gamestate(screen, gamestate)
        clock.tick(MAX_FPS)
        pg.display.flip()


def draw_gamestate(screen, gamestate):
    draw_squares(screen)
    draw_pieces(screen, gamestate.board)


# draws the squares on the boards
def draw_squares(screen):
    colors = [pg.Color("white"), pg.Color("blue")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            # mod 2 either 0 or 1, starting with a light square in the top left and ending with a dark square on top
            # right
            color = colors[((row + column) % 2)]
            pg.draw.rect(screen, color, pg.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# draws the pieces on the board
def draw_pieces(screen, gs_board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = gs_board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], pg.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
