class Solution:
    def frequencySort(self, s: str) -> str:
        counts =  collections.Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for char, count in counts.items():
            buckets[count].append(char)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for char in buckets[i]:
                res.append(char * i)
        return "".join(res)
        
        