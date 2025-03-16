import sys
import pygame
import numpy as np
from constants import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TACK TOE AI')
screen.fill(BG_COLOR)
class Board:
    def _init_(self):
        self.squares =np.zeros( (ROWS, COLS) )
        self.mark_sqr(1,1,2)
        print(self.squares)
    def mark_sqr(self, row, col, player):
        self.squares[row][col]=player

    def empty_sqr(self, row, col):
        return self.squares[row][col]==0


class Game:
    def _init_(self):
        self.board=Board()
        self.player=1
        self.show_lines()
        
    def show_line(self):
        #vertical
        pygame.drow.line(screen, LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.drow.line(screen, LINE_COLOR,(WIDTH - SQSIZE,0),(WIDTH - SQSIZE,HEIGHT),LINE_WIDTH)
        #horizontal
        pygame.drow.line(screen, LINE_COLOR,(0,SQSIZE),(WIDTH, SQSIZE),LINE_WIDTH)
        pygame.drow.line(screen, LINE_COLOR,(0,HEIGHT - SQSIZE),(WIDTH,HEIGHT - SQSIZE),LINE_WIDTH)
    def draw_fig(self, row, col):
        if self.player==1:
        
            #draw cross
            #desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE-OFFSET, row *SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR,start_desc, end_desc, CROSS_WIDTH)

            #asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE- OFFSET)
            end_asc = (col * SQSIZE + SQSIZE-OFFSET, row *SQSIZE + SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR,start_asc, end_asc, CROSS_WIDTH)
        elif self.player==2:
            center=(col*SQSIZE+SQSIZE//2, row*SQSIZE+ SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIOUS, CIRC_WIDTH)

    def next_turn(self):
        self.player=self.player%2+1
        
def main():
    #object
    game=Game()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = event.pos
                        row = pos[1]//SQSIZE
                        COL = POS[0]//SQSIZE
                        
                        if board.empty_sqr(row, col):
                            board.mark_sqr(row,col,game.player)
                            game.draw_fig(row, col)
                            game.next_turn()
                            
        pygame.display.update()
main()
