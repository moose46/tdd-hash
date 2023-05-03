# https://realpython.com/python-hash-table/
class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.values = capacity * [None]

    def __len__(self):
        return len(self.values)
