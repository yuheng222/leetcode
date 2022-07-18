class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, longest, max_repeat = 0, 0, 0
        char_count = {}
        for r in range(len(s)):
            right_char = s[r]
            char_count[right_char] = 1 + char_count.get(right_char, 0)
            max_repeat = max(max_repeat, char_count[right_char])
            # if more than k, window is shifted to the right without extending the window
            if r - l + 1 - max_repeat > k:
                left_char = s[l]
                char_count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest