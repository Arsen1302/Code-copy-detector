class Solution:
    def solution_278_5(self, nums: List[int]) -> int:
        max_ = 0                  #maximum count
        c = 0                     #counter
        for i in nums:
            if i == 1:
                c += 1
                if max_ < c:
                    max_ = c
            else:
                c = 0
        return max_