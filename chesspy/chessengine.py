import chess as ch

class Engine:

    def __init__(self, board, maxDepth, color):
        self.board = board
        self.maxDepth = maxDepth
        self.color = color

    #recursionfunction, include minimax and al,beta pruning
    def engine(self, candidate, depth):
        if depth == self.maxDepth or self.board.legal_moves.count()==0:
            return self.evalFunct() 

        else:
            #get list of legal moves of current position
            moveList = list(self.board.legal_moves)

            #initialize newCandidate
            newCandidate = None
            if depth % 2 != 0: #to check the player's turn? agent or engine's turn?
                newCandidate = float('-inf')
            else:
                newCandidate = float('inf')

            for i in moveList:
                #Play the move i
                self.board.push(i)

                #get the value of move i
                value = self.engine(newCandidate, depth+1)

                #basic minimax algo:
                #if minimizing (engine's turn)
                if value > newCandidate and depth % 2 != 0:
                    newCandidate = value
                    if depth == 1:
                        mo

        
