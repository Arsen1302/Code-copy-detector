class Solution:
    def solution_220_5_1(self, nums: List[int], m: int) -> int:
        
        def solution_220_5_2(maxLimit):
            summ = 0
            div = 1
            for i in nums:
                summ += i
                if summ > maxLimit:
                    summ = i
                    div += 1
            return div
        
        low,high = max(nums),sum(nums)
        
        while low<=high:
            mid = (low+high)//2
            if solution_220_5_2(mid) > m:
                low = mid + 1
            else:
                high = mid - 1
        return low