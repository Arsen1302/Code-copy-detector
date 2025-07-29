class Solution:
    def solution_274_5(self, nums: List[int], k: int) -> List[float]:
        sum_ = 0
        length = len(nums)
        for idx, val in enumerate(nums):
            if idx > length-k:
                break
            temp = sorted(nums[idx:idx+k])
            if k%2==0:
                nums[idx] = (temp[k//2]+temp[k//2-1])/2
            else:
                nums[idx] = temp[k//2]
        if k==1:
            return nums
        return nums[:-k+1]