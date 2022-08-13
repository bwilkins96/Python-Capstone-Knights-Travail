from tree import Node

class KnightPathFinder:
    def __init__(self, pos):
        #self._coordinates = pos
        self._root = pos
        self._considered_positions = {pos}

    def get_valid_moves(self, pos):
        (x, y) = pos
        valid_moves = []

        if x < 7 and y < 6:
            valid_moves.append((x+1,y+2))
        if x < 6 and y < 7:
            valid_moves.append((x+2,y+1))

        if x > 0 and y < 6:
            valid_moves.append((x-1,y+2))
        if x > 1 and y < 7:
            valid_moves.append((x-2,y+1))




finder = KnightPathFinder((0, 0))
#print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
finder.get_valid_moves
