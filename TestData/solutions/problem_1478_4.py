class Solution:
    def solution_1478_4(self, nums: List[int]) -> List[int]:
        ans = []
        freq_count = Counter(nums)
        nums.sort()
        n = len(nums)
        for i in range(n):
            val = nums[i]
            if freq_count[val] == 1 and (i == 0 or nums[i-1] != val-1) and (i == n-1 or nums[i+1] != val+1):
                ans.append(val)
        return ans