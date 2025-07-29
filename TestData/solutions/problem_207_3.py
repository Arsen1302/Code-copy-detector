class Solution:
    def solution_207_3(self, A: List[int]) -> int:
        ans = val = sum(i*x for i, x in enumerate(A))
        ss = sum(A)
        for x in reversed(A):
            val += ss - len(A)*x
            ans = max(ans, val)
        return ans