class Solution:
    def solution_651_1(self, x: int, y: int, bound: int) -> List[int]:
        bx = int(log(bound)/log(x)) if x > 1 else 0
        by = int(log(bound)/log(y)) if y > 1 else 0 
        
        ans = set()
        for i in range(bx+1): 
            for j in range(by+1):
                if x**i + y**j <= bound: 
                    ans.add(x**i + y**j)
        return ans