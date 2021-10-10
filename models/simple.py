import copy

class Node:
    def __init__(self, state):
        self.state = Node.copy_state(state)
        self.turn = state.turn
        self.children = []
        self.has_children = False
        self.score = 0
        self.plays = 0
        self.parent = None

    @staticmethod
    def copy_state(self, state):
        return copy.deepcopy(state)