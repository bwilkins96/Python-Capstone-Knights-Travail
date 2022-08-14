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

        if x > 0 and y > 1:
            valid_moves.append((x-1,y-2))
        if x > 1 and y > 0:
            valid_moves.append((x-2,y-1))

        if x < 7 and y > 1:
            valid_moves.append((x+1,y-2))
        if x < 6 and y > 0:
            valid_moves.append((x+2,y-1))

        return valid_moves

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        moves = set(filter(lambda c: c not in self._considered_positions, valid_moves))

        for m in moves:
            self._considered_positions.add(m)

        return moves


    def build_move_tree(self):
        queue = [(0,0)]
        self._root = Node((0,0))
        parent = self._root

        while len(queue) > 0:
            current = queue.pop(0)
            moves = self.new_move_positions(current)

            if parent._value != current:
                parent = self._root.breadth_search(current)

            for m in moves:
                queue.append(m)
                Node(m).parent = parent




#finder = KnightPathFinder((0, 0))
#finder.build_move_tree()
#print(finder._root.children)
#print(finder._root.children[0].children[0].children)
#print(finder._considered_positions)


#finder = KnightPathFinder((0, 0))
#print (finder._considered_positions)
#print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
#print(finder.get_valid_moves((0,0)))
#print (finder._considered_positions)

#print('\n-----------------------\n')
#finder2 = KnightPathFinder((0,0))
#print(finder2.new_move_positions((4,3)))
