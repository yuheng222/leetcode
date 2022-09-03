class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count, t_count = collections.Counter(), collections.Counter(t)
        res = []
        l, r = 0, 0
        while r < len(s):
            s_count[s[r]] += 1
            r += 1
            if s_count & t_count != t_count:
                continue
            while l < r:
                s_count[s[l]] -= 1
                l += 1
                if s_count & t_count == t_count:
                    continue
                res.append(s[l-1:r])
                break
        if not res:
            return ""
        return min(res, key=len)