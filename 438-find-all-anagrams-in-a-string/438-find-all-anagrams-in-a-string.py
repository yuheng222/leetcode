class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pattern_counter = collections.Counter(p)
        window_counter =  collections.Counter(s[:len(p)])
        res = []
        
        if window_counter == pattern_counter:
            res.append(0)
        
        window_start = 0
        
        for window_end, letter in enumerate(s[len(p):]):
            window_counter[letter] += 1
            window_start_char = s[window_start]
            window_counter[window_start_char] -= 1
            if window_counter[window_start_char] == 0:
                del window_counter[window_start_char]
            window_start += 1
            if window_counter == pattern_counter:
                res.append(window_start)
        
        return res
            
            