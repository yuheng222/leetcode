class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        longest = 0
        char_map = {}
        for r in range(len(s)):
            right_char = s[r]
            if right_char in char_map:
                l = max(l, char_map[right_char] + 1)
            char_map[right_char] = r
            longest = max(longest, r - l + 1)
        return longest
            