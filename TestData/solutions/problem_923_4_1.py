class Solution:
    @lru_cache(None)
    def solution_923_4_1(self,x):
        total = 0

        while x > 1:
            total += 1

            if x%2 == 0:
                x = x//2
            else:
                x = 3*x + 1

        return total

    def solution_923_4_2(self, lo, hi, k):
        ans = [i for i in range(lo,hi+1)]
        ans.sort(key = lambda x: self.solution_923_4_1(x))
        return ans[k-1]