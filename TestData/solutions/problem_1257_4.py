class Solution:
    def solution_1257_4(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        f = start
        b = start
        idx = None
        while f < n or b >= 0:
            if f < n:
                if nums[f] == target:
                    idx = f
                    break
                f += 1
            if b >= 0:
                if nums[b] == target:
                    idx  = b
                    break
                b -= 1
        return abs(idx-start)