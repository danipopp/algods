class RobinHoodHashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            # index is empty
            if entry is None:
                self.table[index] = (key, value, probe_distance)
                return
            
            exist_key, exist_value, exist_distance = entry

            # update existing key
            if exist_key == key:
                self.table[index] = (key, value, exist_distance)
                return
            
            # robin hood condition
            if exist_distance < probe_distance:
                # steal slot
                self.table[index] = (key, value, probe_distance)

                # find new spot
                key = exist_key
                value = exist_value
                probe_distance = exist_distance
            
            # Move index to next slot
            index = (index + 1) % self.capacity
            probe_distance += 
            
    def get(self, key):
        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            if entry is None:
                return None
            
            k, value, distance = entry

            if distance < probe_distance:
                return None
            
            if key == k:
                return value

            index = (index + 1) % self.capacity
            probe_distance += 1