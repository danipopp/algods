class RobinHoodHashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity
    
    