from ..models.simple import Node
from ..game import *
from mcts_util import *
import time
import random

class SimpleMCTS:
    def __init__(self, root, root_player_turn):
        self.root = root
        self.root_player_turn = root_player_turn
    
    def search(self, timelimit) -> Move:
        curr_time = time.time()
        n: Node = None
        while ((curr_time - time.time()) <= timelimit):
            n = self.selection()
            n = self.expand(n)
            self.rollout_bpg(n, self.root_player_turn)
        
        return (self.final_child_root()).move_from_parent
    
    def selection(self) -> Node:
        n = self.root
        while(n.children):
            n = max(n.children, key=uct_score)
        return n
    
    def expand(self, n: Node) -> Node:
        if not n.has_children:
            n.has_children = not n.has_children
            for m in n.state.get_all_possible_moves():
                tmp = Node(n.state)
                tmp.state.do_move(m)
                tmp.parent = n
                tmp.move_from_parent = m
                n.children.append(tmp)
        
        if not n.children:
            return n
        else:
            return n.children[random.randint(0, len(n.children))]
    
    def rollout_bpg(self, n, root_player_turn) -> None:
        winner = -2
        winner = self._rollout(n)
        self._bpg(winner, n, root_player_turn, draw=0.5, win=1.0)
    
    def _rollout(self, n):
        s = Node.copy_state(n.state)
        turn = n.turn
        win = -1

        while win == -1:
            if (moves := s.get_all_possible_moves()):
                break
            else:
                s.do_move(moves[random.randint(0, len(moves))])
                win = s.update_winner()
                turn = 1 - turn
        return win
    
    def _bpg(self, winner, n, root_player_turn, draw, win) -> None:
        while True:
            n.plays += 1
            if (winner == -1):
                n.score += draw
            elif (winner == root_player_turn):
                n.score += win

            if not n.parent:
                break
            else:
                n = n.parent
    
    def final_child_root(self) -> Node:
        return max(self.root.children, key=lambda n: n.plays)
