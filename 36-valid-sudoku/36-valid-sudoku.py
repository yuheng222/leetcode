class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                value = board[r][c]
                if value == '.':
                    continue
                if value in rows[r]:
                    return False
                rows[r].add(value)
                if value in cols[c]:
                    return False
                cols[c].add(value)
                box_idx = r // 3 * 3 + c // 3
                if value in boxes[box_idx]:
                    return False
                boxes[box_idx].add(value)
        return True
                