class Solution:
    def solution_1661_4(self, nums: List[int]) -> int:
        n, nice = len(nums), 1
        cur_bits = nums[0] 
        l, r = 0, 1
        while r < n:
            nice = max(nice, r - l)
            if cur_bits &amp; nums[r]:
                cur_bits ^= nums[l]
                l += 1
            else:
                cur_bits |= nums[r]
                r += 1
        
        return max(nice, r - l)