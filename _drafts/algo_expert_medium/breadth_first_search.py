from collections import deque
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            current = queue.popleft()
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array



A = Node('A')
A.addChild('B')
A.children[0].addChild('C')
A.children[0].addChild('D')
print(A.breadthFirstSearch([]))



