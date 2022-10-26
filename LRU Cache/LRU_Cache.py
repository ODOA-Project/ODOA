class LRUCache:
    def __init__(self, capacity: int):
        self.key_time_table = []
        self.lru_hash = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lru_hash:
            return -1

        result = self.lru_hash[key]
        self.key_time_table.remove(key)
        self.key_time_table.insert(0, key)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.lru_hash:
            self.key_time_table.remove(key)

        if len(self.key_time_table) >= self.capacity:
            last_key = self.key_time_table.pop()
            self.lru_hash.pop(last_key)

        self.key_time_table.insert(0, key)
        self.lru_hash[key] = value


"""
["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
"""
if __name__ == '__main__':
    lru = LRUCache(2)
    lru.get(2)
    lru.put(2, 6)
    lru.get(1)
    lru.put(1, 5)
    lru.put(1, 2)
    lru.get(1)
    lru.get(2)

