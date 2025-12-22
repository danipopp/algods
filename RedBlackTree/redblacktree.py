RED = "RED"
BLACK = "BLACK"

class Node:
    def __init__(self, key):
        self.key = key
        self.coloar = RED
        self.parent = None
        self.left = None
        self.right = None