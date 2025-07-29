class Solution:
    def solution_1453_1_1(self, n: int, startPos: list[int], s: str) -> list[int]:

        def solution_1453_1_2(s, pos, start, end):
            row, colon = pos
            k = 0
            for i in range(start, end):
                cur = s[i]
                row += (cur == 'D') - (cur == 'U')
                colon += (cur == 'R') - (cur == 'L')
                if not (0 <= row < n and 0 <= colon < n):
                    return k
                k += 1
            return k

        ans = []
        for i in range(len(s)):
            ans.append(solution_1453_1_2(s, startPos, i, len(s)))
        return ans