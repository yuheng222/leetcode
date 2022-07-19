class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        pattern_counter = collections.Counter(s1)
        window_counter = collections.Counter(s2[:n])
        
        if pattern_counter == window_counter:
            return True
        
        window_start = 0
        
        for window_end, value in enumerate(s2[n:]):
            window_counter[value] += 1
            window_start_char = s2[window_start]
            window_counter[window_start_char] -= 1
            if window_counter[window_start_char] == 0:
                del window_counter[window_start_char]
            window_start += 1
            if pattern_counter == window_counter:
                return True
        return False
        
                