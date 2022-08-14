class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        self._children.append(node)
        node._parent = self

    def remove_child(self, node):
        self._children.remove(node)
        node._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if self._parent:
            self._parent.remove_child(self)

        if parent:
            parent.add_child(self)

    def depth_search(self, value):
        stack = [self]

        while len(stack) > 0:
            current = stack.pop(-1)

            if current.value == value:
                return current

            for i in range(len(current.children)-1, -1, -1):
                stack.append(current.children[i])

    def breadth_search(self, value):
        queue = [self]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.value == value:
                return current

            for n in current.children:
                queue.append(n)


    def __repr__(self):
        return f'<Node: {self.value}>'
