from typing import Hashable, Any


class HashTable:
    def __init__(self):
        self.size = 8
        self.count = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash_function(self, key: Hashable) -> int:
        return hash(key) % self.size

    def _resize(self, new_size: int) -> None:
        old_keys = self.keys
        old_values = self.values
        self.size = new_size
        self.count = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        for key, value in zip(old_keys, old_values):
            if key is not None:
                self[key] = value

    def set(self, key: Hashable, value: Any) -> None:
        if self.count >= self.size // 2:
            self._resize(self.size * 2)
        if not key.__hash__:
            raise TypeError('Unhashable type')
        index = self._hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                break
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    def get(self, key: Hashable) -> Any:
        index = self._hash_function(key)
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(f"Key '{key}' not found")

    def __getitem__(self, key: Hashable) -> Any:
        return self.get(key)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.set(key, value)


hash_table = HashTable()
hash_table['apple'] = 'Macbook Pro 14'
print(hash_table['apple'])
