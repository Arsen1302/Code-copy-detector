class Solution:
    def solution_1613_2(self, nums: List[int], threshold: int) -> int:
        stack = []
        for hi, x in enumerate(nums + [0]): 
            while stack and stack[-1][1] > x: 
                val = stack.pop()[1]
                lo = stack[-1][0] if stack else -1 
                if val > threshold // (hi - lo - 1): return hi - lo - 1
            stack.append((hi, x))
        return -1