class MyHashSet:

    def __init__(self):
        self.store_len = 10000
        self.store = [[] for i in range(self.store_len)]

    def add(self, key: int) -> None:
        i = hash(key) % self.store_len
        for ex_key in self.store[i]:
            if ex_key == key:
                return 
        
        self.store[i].append(key)

    def remove(self, key: int) -> None:
        i = hash(key) % self.store_len
        if key in self.store[i]:
            self.store[i].remove(key)
        

    def contains(self, key: int) -> bool:
        i = hash(key) % self.store_len
        for ex_key in self.store[i]:
            if ex_key == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)