class Solution:
    def solution_1719_5(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curLcm = nums[i]
            if nums[i] <= k:
                for j in range(i, len(nums)):
                    if nums[j] <= k:
                        curLcm = lcm(curLcm, nums[j])
                        if curLcm == k:
                            res += 1
                    else:
                        break
        return res