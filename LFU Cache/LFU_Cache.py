from collections import defaultdict
from collections import OrderedDict
from typing import Any


class UnSafeLFUCache:

    class Data:
        def __init__(self, key: int, value: Any, count: int):
            self.key: int = key
            self.value: Any = value
            self.freq_count: int = count

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.data_dict: dict = {}
        self.count_key_dict: dict[int] = defaultdict(OrderedDict)
        self.base_count: int = 0

    def get(self, key: int) -> int:
        if key not in self.data_dict:
            return -1

        self._update(key)

        return self.data_dict[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return None

        if key in self.data_dict:
            self.data_dict[key].value = value
            self._update(key)
            return None

        if len(self.data_dict) >= self.capacity:
            self._clear()

        data = self.Data(key, value, 1)
        self.count_key_dict[1][key] = data
        self.data_dict[key] = data
        self.base_count = 1

        return None

    def _update(self, key: int) -> None:
        data = self.data_dict[key]
        freq_count = data.freq_count
        del self.count_key_dict[freq_count][key]

        if len(self.count_key_dict[freq_count]) == 0:
            del self.count_key_dict[freq_count]

        data.freq_count += 1
        self.count_key_dict[data.freq_count][key] = data

        if not self.count_key_dict[self.base_count]:
            self.base_count += 1

        return None

    def _clear(self) -> None:
        key, _ = self.count_key_dict[self.base_count].popitem(last=False)
        del self.data_dict[key]

        return None
