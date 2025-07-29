class Solution:
    def solution_1584_5(self, nums: List[int], k: int) -> int:
        ans = 1

        nums = list(set(nums))
        nums.sort()

        newNums = []
        newNums.append(nums[0])
        nums.pop(0)
        i = 1

        while len(nums) >= 1:
            if nums[0] <= newNums[ans - 1] + k:
                nums.pop(0)
            else:
                ans += 1
                newNums.append(nums[0])
                nums.pop(0)
        
        return ans