class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
        
            