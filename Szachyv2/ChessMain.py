import pygame as py

from Szachyv2 import ChessEngine
#General data used to create board
WIDTH = HEIGHT = 512
DIMENSIONS = 8
SQ_SIZE = WIDTH / DIMENSIONS
MAX_FPS = 10
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN' , 'wB', 'wQ', 'wK','bp', 'bR', 'bN' , 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = py.image.load("C:/Users/przem/PycharmProjects/Szachyv2/Szachyv2/images/" + piece + ".png")

def main():
    py.init()
    screen = py.display.set_mode((WIDTH,HEIGHT))
    gs = ChessEngine.GameState()
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    loadImages()
    running = True
    sq_selected = ()
    playerClicks = []
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                location = py.mouse.get_pos()
                col = int(location[0]//SQ_SIZE)
                row = int(location[1]//SQ_SIZE)
                if sq_selected == (row, col):
                    sq_selected = ()
                    playerClicks = []
                else:
                    sq_selected = (row,col)
                    playerClicks.append(sq_selected)
                    print(sq_selected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sq_selected = ()
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        py.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors=[py.Color("white"), py.Color("grey")]
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            color = colors[((i+j) % 2)]
            py.draw.rect(screen, color, py.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            piece = board[i][j]
            if piece != "--":
                screen.blit(IMAGES[piece], py.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()

