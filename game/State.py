from constants.game_constants import FIRST_PLAYER, NOWINNER
from ..constants import *
from Move import Move
import copy

class State:
    def __init__(self):
        self.game = self.setup_game()
        self.winner = NOWINNER
        self.turn = FIRST_PLAYER
        self.turn_num = 0
    
    def setup_game(self):
        '''The game to setup. For example, on a board
        game this may involve creating a 2D matrix to
        represent a board state.'''
        pass

    def copy_game(self):
        '''
        An optional method to implement. Makes a deepcopy of the
        inner game state.
        '''
        return copy.deepcopy(self.game)
    
    def do_move(self, move: Move):
        '''
        Parses the move and modifies the internal state.
        '''
        pass

    def get_all_possible_moves(self):
        '''
        Returns a list of legal Moves for the current state.
        '''
        pass
    
    def get_random_move(self):
        '''
        Returns a random legal Move for the current state.
        '''
        pass
    
    def update_winner(self):
        '''
        Updates the winner according to the current state.
        '''
        self.winner = self.winner