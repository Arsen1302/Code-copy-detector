class Solution:
    def solution_1701_5(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        evenNums,oddNums=[],[]
        evenTarget,oddTarget=[],[]
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                evenNums.append(nums[i])
            else:
                oddNums.append(nums[i])
            if target[i]%2==0:
                evenTarget.append(target[i])
            else:
                oddTarget.append(target[i])
        ans=0
        for i in range(len(evenNums)):
            ans+=abs(evenNums[i]-evenTarget[i])//2
        for i in range(len(oddNums)):
            ans+=abs(oddNums[i]-oddTarget[i])//2
        return ans//2