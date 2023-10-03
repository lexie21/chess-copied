import pygame
import sys

from const import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()


    def mainloop(self):

        game = self.game
        screen = self.screen
        board = game.board
        dragger = game.dragger

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            #ah this fixes the prob becos it is right next to show_bg, no lag?
            if dragger.dragging:
                dragger.update_blit(screen,size=128)
                # game.show_moves(screen)
            
            # else:
            #     dragger.update_blit(screen,size=80)

            for event in pygame.event.get():
                #clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece #stay the same
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        # board.calc_moves(piece,clicked_row,clicked_col)'
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                    # print(event.pos)
                
                #aha, have to check if mousedown => dragging = True to activate mousemotion()
                #becos mouse motion is yes all the time

                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # dragger.update_blit(screen) #but rendering still in game?

                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                #quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainloop()