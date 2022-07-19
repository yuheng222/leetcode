class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_duration = 0
        for i in range(len(timeSeries) - 1):
            total_duration += min(duration, timeSeries[i+1] - timeSeries[i])
        total_duration += duration
        return total_duration
            