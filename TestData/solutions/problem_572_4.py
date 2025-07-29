class Solution:
    def solution_572_4(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[r0, c0]]
        c_r, c_c = r0, c0  # current row, current column
        s, d = 1, 1  # step, direction

        while len(res) < R * C:
            for _ in range(s):
                c_c = c_c + 1 * d
                if 0 <= c_r < R and 0 <= c_c < C:
                    res.append([c_r, c_c])

            for _ in range(s):
                c_r = c_r + 1 * d
                if 0 <= c_r < R and 0 <= c_c < C:
                    res.append([c_r, c_c])

            s += 1
            d *= -1

        return res