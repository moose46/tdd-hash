# https://realpython.com/python-hash-table/

from typing import Any, NamedTuple

BLANK = None


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be a positive number > 0")
        self._pairs = capacity * [None]

    def __len__(self):
        """ "
        To make the capacity independent from the length, modify your special method .__len__()
        so that it refers to the public property with filtered pairs instead of the private list of all slots:
        """
        return len(self.pairs)

    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = Pair(key, value)
        # print(self.values)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is BLANK:
            raise KeyError(key)
        return pair.value

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
            self._pairs[self._index(key=key)] = BLANK
        else:
            raise KeyError(key)

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def pairs(self):
        """
        You don’t need an explicit call to .copy()
        because the list comprehension creates a new list.
        For every pair in the original list of the key-value pairs,
        you check if that particular pair is truthy
        and keep it in the resulting list.
        However, this will break two other tests that you need to update now:
        """
        return {pair for pair in self._pairs if pair}

    @property
    def values(self):
        """
        Notice that you no longer have to specify the optional filtering condition here,
        because there’s already one lurking behind the .pairs property.
        """
        return [pair.value for pair in self.pairs]

    @property
    def capacity(self):
        return len(self._pairs)

    def _index(self, key):
        return hash(key) % self.capacity
