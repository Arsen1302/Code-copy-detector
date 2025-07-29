class Solution:
    def solution_681_1(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = {(r, c) for r, c in lamps}
        
        row, col, left, right = dict(), dict(), dict(), dict()
        for r, c in lamps:
            row[r] = row.get(r, 0) + 1
            col[c] = col.get(c, 0) + 1
            left[r - c] = left.get(r - c, 0) + 1
            right[r + c] = right.get(r + c, 0) + 1

        res = list()
        for qr, qc in queries:
            if row.get(qr, 0) or col.get(qc, 0) or left.get(qr - qc, 0) or right.get(qr + qc, 0):
                res.append(1)
            else:
                res.append(0)

            for r, c in product(range(qr - 1, qr + 2), range(qc - 1, qc + 2)):
                if (r, c) in lamps:
                    lamps.remove((r, c))
                    row[r] -= 1
                    col[c] -= 1
                    left[r - c] -= 1
                    right[r + c] -= 1

        return res