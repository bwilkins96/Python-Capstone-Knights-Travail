from tree import Node

class KnightPathFinder:
    def __init__(self, pos):
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

    def trace_to_root(self, node):
        route = [node.value]
        current = node

        while current._parent:
            route.append(current._parent.value)
            current = current._parent

        return list(reversed(route))

    def find_path(self, end_position):
        node = self._root.breadth_search(end_position)
        route = self.trace_to_root(node)
        return route


#finder = KnightPathFinder((0, 0))
#finder.build_move_tree()
#print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
#print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
#print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
#print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
