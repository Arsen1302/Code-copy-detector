class Solution:
    def solution_1697_3(self, nums: List[int], minK: int, maxK: int) -> int:
        bad, mi, ma, t = -1, -1, -1, 0
        for right in range(len(nums)):
            if nums[right] == minK:
                mi=right
            if nums[right] == maxK:
                ma=right
            if nums[right] > maxK or nums[right] < minK:
                bad=right
            elif mi >= 0 and ma >= 0:
                lmin = bad + 1
                lmax = min(mi, ma)
                if lmin<=lmax:
                    t+=1 + lmax-lmin
        return t