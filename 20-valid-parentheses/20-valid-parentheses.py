class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for bracket in s:
            if bracket in brackets_map:
                stack.append(bracket)
            elif stack and bracket == brackets_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        