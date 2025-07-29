class Solution:
    def solution_698_3(self, nums: List[int]) -> List[bool]:
        res = []
        n = 0
        for i in nums:
            n *= 2
            if i == 1:
                n += 1
            res.append(n % 5 == 0)
        return res