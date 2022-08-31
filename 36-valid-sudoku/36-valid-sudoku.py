class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                value = board[r][c]
                if value == ".":
                    continue
                if value in rows[r]:
                    return False
                rows[r].add(value)
                if value in cols[c]:
                    return False
                cols[c].add(value)
                boxes_idx = r // 3 * 3 + c // 3
                if value in boxes[boxes_idx]:
                    return False
                boxes[boxes_idx].add(value)
        return True