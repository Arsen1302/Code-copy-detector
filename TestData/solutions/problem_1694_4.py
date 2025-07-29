class Solution:
    def solution_1694_4(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0)+1
        
        ans = -1
        for i in sorted(d.keys()):
            if i<0:
                continue
            elif i>0 and -i in d:
                ans = i
        
        return ans