class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        bucket, i = self.getBucketIndex(key)
        if i < 0:
            bucket.append((key, value))
        else:
            bucket[i] = (key, value)

    def get(self, key: int) -> int:
        bucket, i = self.getBucketIndex(key)
        if i < 0:
            return -1
        else:
            return bucket[i][1]

    def remove(self, key: int) -> None:
        bucket, i = self.getBucketIndex(key)
        if i < 0:
            return
        else:
            bucket.remove(bucket[i])
            
    def getBucketNum(self, key):
        return key % self.size
    
    def getBucketIndex(self, key):
        bucketNum = self.getBucketNum(key)
        bucket = self.buckets[bucketNum]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1


# [[(19: 20)], [], ...[]] x 2069
    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)