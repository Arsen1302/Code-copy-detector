class Solution:
    def solution_1363_2(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    ans += freq[nums[k] - nums[i] - nums[j]]
            freq[nums[i]] += 1
        return ans