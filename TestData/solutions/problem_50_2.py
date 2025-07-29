class Solution:
    def solution_50_2(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for a,b in d.items():
            print(a,b)
            if b == 1:
                return a