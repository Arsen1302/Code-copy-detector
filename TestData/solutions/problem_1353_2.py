class Solution:
    def solution_1353_2(self, nums: List[str]) -> str:
        ans = []
        for i, x in enumerate(nums): 
            if x[i] == "1": ans.append("0")
            else: ans.append("1")
        return "".join(ans)