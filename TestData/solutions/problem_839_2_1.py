class Solution:
    def solution_839_2_1(self, nums: List[int], threshold: int) -> int:
        def solution_839_2_2(mid):
            ans = 0
            for num in nums:
                ans += math.ceil(num / mid)
                if ans > threshold: return False
            return True    
        l, r = 1, int(1e6)
        while l <= r:
            mid = (l+r) // 2
            if solution_839_2_2(mid): r = mid - 1
            else: l = mid + 1
        return l