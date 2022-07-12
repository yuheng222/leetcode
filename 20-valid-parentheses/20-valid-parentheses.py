class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for bracket in s:
            if bracket not in brackets_map:
                stack.append(bracket)
            elif stack and stack[-1] == brackets_map[bracket]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
                