class Solution:
    def solution_1589_2(self, nums: List[int], k: int) -> int:
        nums += [k]
        slow = cur = ans = 0
        for i, num in enumerate(nums):
            cur += num
            while cur * (i - slow + 1) >= k:
                ans += i - slow 
                cur -= nums[slow]
                slow += 1
        return ans