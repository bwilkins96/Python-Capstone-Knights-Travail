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


#node1 = Node("root1")
#node2 = Node("root2")
#node3 = Node("root3")

#node3.parent = node1
#node3.parent = node2

#print(node1.children)
#print(node2.children)

#for i in range(5, -1, -1):
#    print(i)

""" test = Node(1)
test2 = Node(2)
test3 = Node(3)
test4 = Node(4)
test5 = Node(5)
test6 = Node(6)
test7 = Node(7)
test8 = Node(8)
test9 = Node(9)
test10 = Node(10)

#test.add_child(test2)
test2.parent = test
test.add_child(test3)
test.add_child(test4)

test2.add_child(test5)
test3.add_child(test6)
test4.add_child(test7)

test5.add_child(test8)
test5.add_child(test9)

test8.add_child(test10) """

#test.depth_search(7)
#test.breadth_search(10)
