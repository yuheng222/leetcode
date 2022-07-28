class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        # sort the intervals using the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end: # overlapping interval
                end = max(interval[1], end)
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        merged.append([start, end]) # add last interval
        return merged