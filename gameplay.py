import pygame as p

SQ_SIZE = 64
WIDTH = SQ_SIZE*25
HEIGHT = SQ_SIZE*13
MAX_FPS = 15
DIMENSION = 11
TEXT = {}
class GameState():
    def __init__(self):
        self.board = [
            ["-","1","2","3","4","5","6","7","8","9","10"],
            ["A","-","-","-","-","-","-","-","-","-","-"],
            ["B","-","-","-","-","-","-","-","-","-","-"],
            ["C","-","-","-","-","-","-","-","-","-","-"],
            ["D","-","-","-","-","-","-","-","-","-","-"],
            ["E","-","-","-","-","-","-","-","-","-","-"],
            ["F","-","-","-","-","-","-","-","-","-","-"],
            ["G","-","-","-","-","-","-","-","-","-","-"],
            ["H","-","-","-","-","-","-","-","-","-","-"],
            ["I","-","-","-","-","-","-","-","-","-","-"],
            ["J","-","-","-","-","-","-","-","-","-","-"]]
        self.firstpersonMove = True
        self.moveLog = []
def main():
    p.init()
    font = p.font.SysFont('consolas', 50)
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    p.display.set_caption("WARSHIP")
    loadText(font)
    gs = GameState()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def loadText(font):
    pieces = ["1","2","3","4","5","6","7","8","9","10","A","B","C","D","E","F","G","H","I","J"]
    for piece in pieces:
        TEXT[piece] = font.render(piece, True, (0,0,0))

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board,1)
    drawPieces(screen, gs.board,13)

def drawBoard(screen):
    color = p.Color("grey")
    Board(screen,color,1)
    Board(screen,color,13)
            
def Board(screen,color,k):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            p.draw.rect(screen, color, p.Rect((c+k)*SQ_SIZE,(r+1)*SQ_SIZE,SQ_SIZE,SQ_SIZE), 1)

def drawPieces(screen, board,k):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "-":
                screen.blit(TEXT[piece], p.Rect((c+k)*SQ_SIZE, (r+1)*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
    main()
