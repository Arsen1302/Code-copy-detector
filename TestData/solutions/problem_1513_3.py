class Solution:
    def solution_1513_3(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            gcd = math.gcd(nums[i], nums[i + 1])
            if gcd > 1:
                nums[i] = abs(nums[i] * nums[i + 1]) // gcd  # lcm
                del nums[i + 1]
                i = max(0, i - 1)
            else:
                i += 1
        return nums