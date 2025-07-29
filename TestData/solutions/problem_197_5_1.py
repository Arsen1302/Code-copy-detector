class Solution:
    def solution_197_5_1(self, n: int) -> List[int]:
        
        def solution_197_5_2(x):
            """Pre-order traverse the tree."""
            if x <= n:
                ans.append(x)
                for xx in range(10): solution_197_5_2(10*x + xx)
        
        ans = []
        for x in range(1, 10): solution_197_5_2(x)
        return ans