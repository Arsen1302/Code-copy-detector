class Solution:
    def solution_534_2(self, nums: List[int], k: int) -> bool:
        nums.sort()
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
        for i in range(n):
            if count[nums[i]] != 0:
                count[nums[i]] -= 1
                for j in range(nums[i]+1, nums[i]+k):
                    if count[j] == 0:
                        return False
                    count[j] -= 1
        return True