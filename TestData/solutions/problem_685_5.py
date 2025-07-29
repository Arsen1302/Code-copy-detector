class Solution:
    def solution_685_5(self, nums: List[int], k: int) -> int:

        less = False
        for i in nums:
            if i < 0:
                less = True
                break
        
        nums.sort(key = lambda x : abs(x))

        if not less:
            if k % 2 == 0:
                return sum(nums)
            else:
                return sum(nums[1:]) - nums[0]

        i = len(nums) - 1
        while(k > 0):
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            i -= 1

            if i == 0 and k > 0:
                if nums[0] > 0:
                    if k % 2 == 0:
                        break
                    else:
                        nums[0] *= -1
                        break
                else:
                    if k % 2 == 0:
                        break
                    else:
                        nums[0] *= -1
                        break

        return sum(nums)