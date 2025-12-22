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
    