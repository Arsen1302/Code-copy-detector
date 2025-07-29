class Solution:
    def solution_1056_4_1(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = [0]
        for i in range(n):
            pre.append(stoneValue[i] + pre[-1])
        @lru_cache(None)
        def solution_1056_4_2(l, r):
            if r <= l:
                return 0
            res = 0
            for i in range(l, r):
                # [l, i] [i + 1, r]
                left = pre[i + 1] - pre[l]
                right = pre[r + 1] - pre[i + 1]
                if right > left:
                    res = max(res, solution_1056_4_2(l, i) + left)
                elif left > right:
                    res = max(res, solution_1056_4_2(i + 1, r) + right)
                else:
                    res = max(res, solution_1056_4_2(l, i) + left)
                    res = max(res, solution_1056_4_2(i + 1, r) + right)
            return res
        return solution_1056_4_2(0, n - 1)