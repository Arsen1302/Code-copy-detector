class Solution:
    def solution_1634_1(self, nums: List[int]) -> int:
        
        n = len(nums)
        k = nums[n - 1]
        ans = 0
        
        for i in reversed(range(n - 1)):
            if nums[i] > k:
                l =  nums[i] / k
                if l == int(l):
                    ans += int(l) - 1
                    k = nums[i] / int(l)
                else:
                    ans += int(l)
                    k = int(nums[i] / (int(l) + 1))
            else:
                k = nums[i]

        return ans