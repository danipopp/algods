class RobinHoodHashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.table = [None] * capacity

        