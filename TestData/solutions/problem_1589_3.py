class Solution:
    def solution_1589_3(self, xs: List[int], k: int) -> int:
        n = len(xs)

        i, j, sub_sum = 0, 0, 0
        ans = 0
        while j < n:
            sub_sum += xs[j]
            if sub_sum * (j - i + 1) < k:
                ans += j - i + 1
                j += 1
            elif i == j:
                sub_sum = 0
                j += 1
                i = j
            else:
                sub_sum -= xs[i] + xs[j]
                i += 1
                
        return ans