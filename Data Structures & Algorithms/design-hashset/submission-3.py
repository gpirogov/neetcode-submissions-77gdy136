class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10)] #arbitrarily choosing 10 for # of buckets

    def add(self, key: int) -> None:
        if key not in self.buckets[key % len(self.buckets)]:
            self.buckets[key % len(self.buckets)].append(key)

    def remove(self, key: int) -> None:
        # O(n) time
        if key in self.buckets[key % len(self.buckets)]:
            self.buckets[key % len(self.buckets)].remove(key)

    def contains(self, key: int) -> bool:
        # O(n) time
        if key in self.buckets[key % len(self.buckets)]:
           return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)