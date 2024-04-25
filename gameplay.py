import pygame as p
import time

SQ_SIZE = 64
WIDTH = SQ_SIZE * 25
HEIGHT = SQ_SIZE * 13
MAX_FPS = 15
DIMENSION = 11
TEXT = {}
a = time.time()
checking = 0
sqSelected=()
choose_piece={}
clicking_session=0
clicking_state=False
class GameState():
    def __init__(self):
        self.board = [
            ["-", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10"],
            [" A", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" B", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" C", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" D", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" E", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" F", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" G", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" H", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" I", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            [" J", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        self.firstpersonMove = True
        self.moveLog = []


def main():
    global clicking_session,clicking_state
    p.init()
    font = p.font.SysFont('Sans', SQ_SIZE - 8)
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    p.display.set_caption("WARSHIP")
    loadText(font)
    gs = GameState()
    sqSelected = ()
    playerClick = []
    running = True
    while running:
        screen.fill(p.Color("white"))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                clicking_session+=1
                clicking_state=True

            elif e.type==p.MOUSEBUTTONUP:
                clicking_state=False
            if clicking_state:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if frozenset((row*100,col)) in choose_piece:
                    if choose_piece[frozenset((row*100,col))]!=clicking_session:
                        del choose_piece[frozenset((row*100,col))]
                else:
                    choose_piece[frozenset((row*100, col))]=clicking_session
            #print(choose_piece,clicking_session,clicking_state)

        drawGameState(screen, gs,sqSelected)
        if checking == 0:
            readymode(font, screen)
            # danh dau
        if checking == 1:
            pass
        clock.tick(MAX_FPS)
        p.display.flip()


def readymode(font, screen):
    timing(60, font, screen)


def settiming(secs):
    return secs - (time.time() - a)


def timing(secs, font, screen):
    text_time = font.render(str(int(settiming(secs))), True, (0, 0, 0))
    screen.blit(text_time, (12 * SQ_SIZE, 0))


def loadText(font):
    pieces = [" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " A", " B", " C", " D", " E", " F", " G",
              " H", " I", " J"]
    for piece in pieces:
        TEXT[piece] = font.render(piece, True, (0, 0, 0))


def drawGameState(screen, gs,sqSelected):
    drawBoard(screen,sqSelected)
    drawPieces(screen, gs.board, 1)
    drawPieces(screen, gs.board, 13)


def drawBoard(screen,sqSelected):
    color = p.Color("grey")
    Board(screen, color, 1,sqSelected)
    Board(screen, color, 13,sqSelected)


def Board(screen, color, k,sqSelected):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if frozenset(((r+k)*100,c+k)) in choose_piece:
                p.draw.rect(screen,color , p.Rect((c + k) * SQ_SIZE, (r + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE), 0)
            else:
                p.draw.rect(screen, color, p.Rect((c + k) * SQ_SIZE, (r + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)


def drawPieces(screen, board, k):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "-":
                screen.blit(TEXT[piece], p.Rect((c + k) * SQ_SIZE, (r + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
