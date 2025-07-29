class Solution:
    def solution_1583_2(self, nums: List[int]) -> int:
        n=len(nums)
        
        newNums=[]*n
        while(n!=1):
            n=n//2
            newNums=[]*n
            for i in range(n):
                if i%2==0:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums=newNums
        return nums[0]