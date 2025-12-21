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
            probe_distance += 1
            
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

    def remove(self, key):
        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            if entry is None:
                return
            
            k, v, distance = entry
            
            if distance < probe_distance:
                return
            
            if k == key:
                self.shift_delete(index)
                return
            
            index = (index + 1) % self.capacity
            probe_distance += 1

    def shift_delete(self, start):
        index = start
        
        while True:
            next_index = (index + 1) % self.capacity
            next_entry = self.table[next_index]

            if next_entry is None or next_entry[2] == 0:
                self.table[index] = None
                return
            
            k, v, dist = next_entry
            self.table[index] = (k, v, dist - 1)
            index = next_index