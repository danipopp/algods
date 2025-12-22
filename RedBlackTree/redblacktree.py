RED = "RED"
BLACK = "BLACK"

class Node:
    def __init__(self, key):
        self.key = key
        self.colar = RED
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.colar = BLACK
        self.root = self.NIL

    # -------------- Rotations --------------
    def left_rotation(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y