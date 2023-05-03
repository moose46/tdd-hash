# https://realpython.com/python-hash-table/

BLANK = object()


class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        self.values[self._index(key)] = value
        # print(self.values)

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        # print(f"index={self._index}")
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def _index(self, key):
        return hash(key) % len(self)
