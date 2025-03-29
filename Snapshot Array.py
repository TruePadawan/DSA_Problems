'''
(Memory Limit Exceeded)
At every call of snap,
store current array in hash table with key being the snap_id
'''

'''
Rather than storing the array at each snapshot
Let's keep track of the changes to the array and store that at each snapshot
If a call to get() is for an index that has not been changed at the current snap_id:
    Check previous snapshots for the latest change:
        If none found, return 0
'''

class SnapshotArray:
    def __init__(self, length: int):
        # self.array = []
        self.snapshots = {}
        self.changes = {}
        self.snap_id = 0
        # for i in range(length):
        #     self.array.append(0)

    def set(self, index: int, val: int) -> None:
        # self.array[index] = val
        self.changes[index] = val

    def snap(self) -> int:
        self.snapshots[self.snap_id] = self.changes.copy()
        self.changes = {}
        # self.snapshots[self.snap_id] = self.array.copy()
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        # Check if there is an update at the specified snap_id
        value = self.snapshots[snap_id].get(index)
        if value is not None:
            return value
        else:
            # Check for the latest update or return 0 if none found
            snap_id -= 1
            while snap_id >= 0:
                value = self.snapshots[snap_id].get(index)
                if value is not None:
                    return value
                snap_id -= 1
            return 0

class OldSnapshotArray:
    def __init__(self, length: int):
        self.array = []
        self.snapshots = {}
        self.snap_id = 0
        for i in range(length):
            self.array.append(0)

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snapshots[self.snap_id] = self.array.copy()
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)