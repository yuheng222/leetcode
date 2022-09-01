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
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()
                if brackets_map[open_bracket] != bracket:
                    return False
        return len(stack) == 0
        