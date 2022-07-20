class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count, t_count = collections.Counter(), collections.Counter(t)
        l, r = 0, 0
        results = []
        # Expand window to try and match the characters in s with t
        while r < len(s):
            s_count[s[r]] += 1
            r += 1
            # if the characters in the window doesn't match, continue expanding the window
            if s_count & t_count != t_count:
                continue
            while l < r:
                s_count[s[l]] -= 1
                l += 1
                # if window still matches the pattern, shrink the window
                if s_count & t_count == t_count:
                    continue
                results.append(s[l-1:r])
                break
        if not results:
            return ""
        return min(results, key=len)