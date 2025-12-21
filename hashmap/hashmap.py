class RobinHoodHashMap:
    """
    Hash map implementation using Robin Hood hashing (open addressing).

    Each entry stored as a tuple:
        (key, value, probe_distance)

    probe_distance = how far the entry is from its original hash index.
    """

    def __init__(self, capacity = 8):
        """
        Initialize the hash map.

        :param capacity: Number of slots in the hash table.
        """
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        """
        Compute the home index for a key.

        :param key: Hashable key
        :return: Index in the table
        """
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """
        Insert or update a key-value pair using Robin Hood hashing.

        If a collision occurs, the entry with the larger probe distance
        steals the slot, and the displaced entry continues probing.
        """

        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            # Case 1: Empty slot found → insert here
            if entry is None:
                self.table[index] = (key, value, probe_distance)
                return
            
            exist_key, exist_value, exist_distance = entry

            # Case 2: Key already exists → update value
            if exist_key == key:
                self.table[index] = (key, value, exist_distance)
                return
            
            # Case 3: Robin Hood condition
            # If the existing entry is closer to its home than we are,
            # we steal the slot and push the existing entry forward.
            if exist_distance < probe_distance:
                # Place the current (key, value) into this slot
                self.table[index] = (key, value, probe_distance)

                # Continue inserting the displaced entry
                key = exist_key
                value = exist_value
                probe_distance = exist_distance
            
            # Move to the next slot (linear probing)
            index = (index + 1) % self.capacity
            probe_distance += 1
            
    def get(self, key):
        """
        Retrieve the value associated with a key.

        Stops searching early if an entry with a smaller probe distance
        is encountered (Robin Hood invariant).
        """
        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            # Empty slot → key not present
            if entry is None:
                return None
            
            k, value, distance = entry

            # If we encounter an entry that is closer to its home than
            # we are, the key cannot exist further in the probe sequence
            if distance < probe_distance:
                return None
            
            # Key found
            if key == k:
                return value

            index = (index + 1) % self.capacity
            probe_distance += 1

    def remove(self, key):
        """
        Remove a key from the hash map.

        After removal, entries are backward-shifted to preserve
        the Robin Hood hashing invariants.
        """

        index = self._hash(key)
        probe_distance = 0

        while True:
            entry = self.table[index]

            # Empty slot → key not present
            if entry is None:
                return
            
            k, v, distance = entry
            
            # Key cannot exist further
            if distance < probe_distance:
                return
            
            # Key found → delete and shift entries
            if k == key:
                self.shift_delete(index)
                return
            
            index = (index + 1) % self.capacity
            probe_distance += 1

    def shift_delete(self, start):
        """
        Perform backward shifting after deletion.

        Moves subsequent entries backward until:
        - an empty slot is found, or
        - an entry with probe_distance == 0 is found
        """
        index = start
        
        while True:
            next_index = (index + 1) % self.capacity
            next_entry = self.table[next_index]

            # Stop shifting when reaching an empty slot
            # or an entry at its home position
            if next_entry is None or next_entry[2] == 0:
                self.table[index] = None
                return
            
            k, v, dist = next_entry

            # Shift entry backward and reduce its probe distance
            self.table[index] = (k, v, dist - 1)
            index = next_index