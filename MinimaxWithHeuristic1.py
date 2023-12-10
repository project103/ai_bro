from Board import Board
import numpy as np
Class MinimaxWithHeuristic1:
    
    def __init__(self):
        self.board = Board()



    def count_ways_to_win(self, player, cell):
        ways_to_win= 0
        ways_to_win += self.count_ways_to_win_in_rows(player)
        ways_to_win += self.count_ways_to_win_in_columns(player)
        ways_to_win += self.count_ways_to_win_in_diagonals(player)
        ways_to_win += self.count_ways_to_win_across_layers(player)
        ways_to_win += self.count_ways_to_win_accross_diagonals_within_layers(player)

    
        #count ways to win in rows
        def count_ways_to_win_in_rows(self, player):
            for layer in board.__board:
                for row in layer:
                    if board.is_win(player):
                        ways_to_win += 1
                        return ways_to_win
    
        #count ways to win in columns
        def count_ways_to_win_in_columns(self, player):
            for col in range(4):
                for layer in board.__board:
                    if board.is_win(player):
                        ways_to_win += 1
                        return ways_to_win
                
        #count ways to win in diagonals
        def count_ways_to_win_in_diagonals(self, player):
            for layer in board.__board:
                if board.is_win(player):
                    ways_to_win += 1
                    return ways_to_win
            
        #count ways to win across layers
        def count_ways_to_win_across_layers(self, player):
            for layer in board.__board:
                if board.is_win(player):
                    ways_to_win += 1
                    return ways_to_win
                
        #count ways to win diagonals between layers
        def count_ways_to_win_accross_diagonals_within_layers(self, player):
            for layer in board.__board:
                if board.is_win(player):
                    ways_to_win += 1
                    return ways_to_win
                
        return ways_to_win
    
    def minimax_heuristic(self, player):
        # Create a list of counts from each way to win function
        counts = [
            self.count_ways_to_win_in_rows(player),
            self.count_ways_to_win_in_columns(player),
            self.count_ways_to_win_in_diagonals(player),
            self.count_ways_to_win_across_layers(player),
            self.count_ways_to_win_accross_diagonals_within_layers(player)
        ]

        # Return the maximum count
        max_index = counts.index(np.max(counts))

        moves = [
            ('rows', 'row'),
            ('columns', 'col'),
            ('diagonals', 'diagonal'),
            ('across_layers', 'layer'),
            ('accross_diagonals_within_layers', 'layer diagonal')
        ]
        return moves[max_index]
    
    def best_move(self, player):
        move = self.minimax_heuristic(player)
        return move