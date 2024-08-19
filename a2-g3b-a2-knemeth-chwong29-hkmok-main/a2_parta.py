#    Main Author(s): 
#    Main Reviewer(s):

class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table


    def __init__(self, capacity=32):
        self._capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def insert(self, key, value):
        index = self._get_hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return False
            index = self._get_hash(index + 1)
        self.table[index] = (key, value)
        self.size += 1
        if self.size / self._capacity > 0.7:
            self._resize()
        return True

    def modify(self, key, value):
        index = self._search_index(key)
        if index < 0:
            return False
        else:
            self.table[index] = (key, value)
            return True

    def remove(self, key):
        index = self._search_index(key)
        if index < 0:
            return False
        self.table[index] = None
        self.size -= 1
        self._rehash_from(index)
        return True

    def _rehash_from(self, index):
        next_index = (index + 1) % self._capacity
        while self.table[next_index] is not None:
            key, value = self.table[next_index]
            self.table[next_index] = None
            self.size -= 1
            self.insert(key, value)
            next_index = (next_index + 1) % self._capacity

    def search(self, key):
        index = self._search_index(key)
        if index < 0:
            return None
        else:
            return self.table[index][1]

    def capacity(self):
        return self._capacity

    def __len__(self):
        return self.size

    def _get_hash(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        new_capacity = self._capacity * 2
        new_table = [None] * new_capacity
        for pair in self.table:
            if pair is not None:
                key, value = pair
                index = hash(key) % new_capacity
                while new_table[index] is not None:
                    index = (index + 1) % new_capacity
                new_table[index] = (key, value)
        self._capacity = new_capacity
        self.table = new_table

    def _search_index(self, key):
        index = self._get_hash(key)
        checked = 0
        while checked < self._capacity:
            if self.table[index] is None:
                return -1
            if self.table[index][0] == key:
                return index
            index = self._get_hash(index + 1)
            checked += 1
        return -1
