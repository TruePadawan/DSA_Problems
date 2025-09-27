from typing import List


class Store:
    data: dict[int, str]
    timestamps: List[int]
    def __init__(self):
        self.data = {}
        self.timestamps = []

    def get(self, timestamp: int) -> str:
        if self.data.get(timestamp) is not None:
            return self.data[timestamp]
        largest_timestamp = self.get_largest_timestamp(timestamp)
        return "" if largest_timestamp == -1 else self.data[largest_timestamp]

    def get_largest_timestamp(self, timestamp: int) -> int:
        i = 0
        j = len(self.timestamps) - 1
        largest_timestamp = -1
        while i <= j:
            middle_idx = (i+j)//2
            middle = self.timestamps[middle_idx]
            if timestamp < middle:
                j = middle_idx - 1
            else:
                i = middle_idx + 1
            if largest_timestamp < middle < timestamp:
                largest_timestamp = middle
        return largest_timestamp


    def set(self, timestamp: int, value: str) -> None:
        self.data[timestamp] = value
        self.timestamps.append(timestamp)


class TimeMap:
    store: dict[str, Store]

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key) is None:
            self.store[key] = Store()
        self.store[key].set(timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        if self.store.get(key) is None:
            return ""
        return self.store[key].get(timestamp)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
