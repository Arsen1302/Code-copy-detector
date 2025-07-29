class Solution:
    def solution_315_4(self, nums: List[int], k: int) -> int:
        d = {}
        for i in nums:
            if d.get(i):
                d[i]+=1
            else:
                d[i] = 1
        ans = 0
        for i in d:
            if d.get(i+k) and (k != 0 or d[i] > 1):
                ans+=1
        return ans