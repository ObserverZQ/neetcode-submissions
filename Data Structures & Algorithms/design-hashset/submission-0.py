class MyHashSet:
    # boolean array, store if the value exists in the set
    def __init__(self):
        # we have key from 0 to 1,000,000, which is 1,000,001 keys
        self.hashset = [False] * 1000001

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)