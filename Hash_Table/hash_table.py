class HashTable:
    def __init__(self):
        self.MAX = 10                      # fixed size of hash table
        self.arr = [None for _ in range(self.MAX)]  # initialize with empty slots

    def get_hash(self, key):
        """Simple hash function: sum of ASCII values mod table size"""
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        """Insert key-value using linear probing"""
        h = self.get_hash(key)

        # If slot is empty or key already exists → store value
        if self.arr[h] is None or self.arr[h][0] == key:
            self.arr[h] = (key, val)
            return

        # Collision → Linear Probing
        start = h
        while True:
            h = (h + 1) % self.MAX
            if self.arr[h] is None or self.arr[h][0] == key:
                self.arr[h] = (key, val)
                return
            if h == start:  # we circled back → table full
                raise Exception("HashTable is full!")

    def __getitem__(self, key):
        """Retrieve value for key using linear probing"""
        h = self.get_hash(key)
        start = h
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h + 1) % self.MAX
            if h == start:  # circled back
                break
        return None  # key not found

    def __delitem__(self, key):
        """Delete key-value pair"""
        h = self.get_hash(key)
        start = h
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return
            h = (h + 1) % self.MAX
            if h == start:
                break
        raise KeyError(f"{key} not found")

    def print_table(self):
        """Helper method to display table"""
        for i, val in enumerate(self.arr):
            print(i, ":", val)
