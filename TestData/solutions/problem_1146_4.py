class Solution:
    def solution_1146_4(self, nums: List[int]) -> int:
        msf = -9999 # max sum so far
        meh = 0 # max sum ending here
        s = set()
        j = 0
        i = 0
        while j < len(nums):
            meh += nums[j]
            while nums[j] in s:
                meh -= nums[i]
                s.remove(nums[i])
                i += 1
            s.add(nums[j])
            if msf < meh:
                msf = meh
            j += 1
        return msf