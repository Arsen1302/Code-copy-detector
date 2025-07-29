class Solution:
    def solution_613_5_1(self, A: List[List[int]]) -> int:
        # dp top down: recursive + memos
        # from start column c: dc = [-1, 0, 1], if c + dc valid
        # get min of solution_613_5_2(r+1, c+dc) iterations
        # base case when row == max, return A[r][c]
        # O(3^M) time, O(3^M) recursive calls
        rows, cols = len(A), len(A[0])

        def solution_613_5_2(r, c):
            if (r,c) in self.cache: return self.cache[(r,c)]
            if r == rows-1: return A[r][c]

            tmp = float("inf")
            for dc in [-1, 0, 1]:
                if 0 <= c+dc < cols:
                    tmp = min(tmp, solution_613_5_2(r+1, c+dc))

            min_sum = A[r][c] + tmp
            self.cache[(r,c)] = min_sum
            return min_sum

        # setup and recursive calls
        self.cache = {}
        res = float("inf")
        for c in range(cols):
            res = min(res, solution_613_5_2(0, c))
        return res

    def solution_613_5_3(self, A: List[List[int]]) -> int:
        # dp bottom up: tabulation (remove the recursive call stack)
        # recursive solution builds up from 0,0 to rows, cols
        # two for loops, both decreasing => answer min of row 0
        # O(MN) time, O(MN) space
        rows, cols = len(A), len(A[0])
        dp = [[float("inf") for _ in range(rows)] for __ in range(cols)]
        dp[rows-1] = A[rows-1]

        for r in range(rows-2, -1, -1):
            for c in range(cols-1, -1, -1):

                tmp = float("inf")
                for dc in [-1, 0, 1]:
                    if 0 <= c+dc < cols:
                        tmp = min(tmp, dp[r+1][c+dc])

                min_sum = A[r][c] + tmp
                dp[r][c] = min_sum

        return min(dp[0])

    def solution_613_5_4(self, A: List[List[int]]) -> int:
        # same as above, but just reuse the existing grid!
        # O(MN) time, O(1) space
        rows, cols = len(A), len(A[0])
        for r in range(rows-2, -1, -1):
            for c in range(cols-1, -1, -1):

                tmp = float("inf")
                for dc in [-1, 0, 1]:
                    if 0 <= c+dc < cols:
                        tmp = min(tmp, A[r+1][c+dc])
                A[r][c] += tmp

        return min(A[0])