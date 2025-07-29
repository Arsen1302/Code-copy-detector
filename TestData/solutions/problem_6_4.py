class Solution:
    def solution_6_4(self, s: str, numRows: int) -> str:
        rows, direction, i = [[] for _ in range(numRows)], 1, 0
        for ch in s:
            rows[i].append(ch)
            i = min(numRows - 1, max(0, i + direction))
            if i == 0 or i == numRows - 1: direction *= -1
        return ''.join(''.join(row) for row in rows)