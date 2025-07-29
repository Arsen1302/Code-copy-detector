class Solution:
    def solution_1619_3(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k, trim in queries: 
            cand = [x[-trim:] for x in nums]
            _, v = sorted(zip(cand, range(len(cand))))[k-1]
            ans.append(v)
        return ans