class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()
                if char_map[open_bracket] != char:
                    return False
        if stack:
            return False
        return True
        