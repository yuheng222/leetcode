class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        s_count, t_count = {}, {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        res, min_len = [-1, -1], float("inf")
        have, need = 0, len(t_count)
        l = 0
        for r in range(len(s)):
            char = s[r]
            s_count[char] = 1 + s_count.get(char, 0)
            if char in t_count and s_count[char] == t_count[char]:
                have += 1
            while have == need:
                # update result
                if r - l + 1 < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                # pop from the left of our window
                s_count[s[l]] -= 1
                # if the popped char was in t_count and now that freq of char in s_count is 0, decrement have
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]
                
        