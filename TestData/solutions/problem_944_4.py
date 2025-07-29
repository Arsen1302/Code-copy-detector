class Solution:
    def solution_944_4(self, nums: List[int]) -> int:
        startValue = 1 + (-1*nums[0])
        while True:
            s = startValue + nums[0]
            for i in nums[1:]:
                s += i
                if s < 1:
                    startValue += 1
                    break
            if s > 0:
                break
        if startValue < 1:
             startValue = 1
        return startValue