class Solution:
    def solution_1170_4(self, nums: List[int]) -> int:
        hasmap = collections.defaultdict(int)
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                hasmap[nums[i]*nums[j]] += 1
        ans = 0
        for val in hasmap.values():
            ans += (8*val*(val-1))//2
        return ans