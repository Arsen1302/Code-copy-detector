class Solution:
    def solution_1029_5(self, s: str, indices: List[int]) -> str:
        ans = [""]*len(s)
        for i, x in zip(indices, s):
            ans[i] = x
        return "".join(ans)