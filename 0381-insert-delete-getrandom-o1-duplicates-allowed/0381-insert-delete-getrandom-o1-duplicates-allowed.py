class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.cache = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        self.cache[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.cache[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False
        last_ele = self.arr[-1]
        idx = self.cache[val].pop()
        self.arr[idx] = last_ele
        self.cache[last_ele].add(idx)
        self.cache[last_ele].discard(len(self.arr) - 1)
        self.arr.pop()
        if len(self.cache[val]) == 0:
            self.cache.pop(val)
        return True

    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.arr) - 1)
        return self.arr[random_idx]
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()