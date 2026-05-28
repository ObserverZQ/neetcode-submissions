class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0
        self.capacity = capacity
    
    def hash(self, key: int) -> int:
        # hash(key) % self.capacity for integers is more efficient
        return hash(key) % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.arr[index] == None:
                self.arr[index] = Pair(key, value)
                self.size += 1
                if self.size >= (self.capacity // 2):
                    self.resize()
                return
            elif self.arr[index].key == key:
                self.arr[index].value = value
                return
            else: # keep looking for empty space in the next indices
                index += 1
                index %= self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.arr[index]:
            if self.arr[index].key == key:
                return self.arr[index].value
            index += 1
            index %= self.capacity
        return -1

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
        index = self.hash(key)
        while True:
            if self.arr[index].key == key:
                self.arr[index] = Pair(-1, -1)
                self.size -= 1
                return True
            index += 1
            index %= self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = []
        for i in range(self.capacity):
            newArr.append(None)
        old = self.arr
        self.arr = newArr
        self.size = 0
        for pair in old:
            if pair:
                self.insert(pair.key, pair.value)
        