class Solution:
    def solution_969_2(self, n: int) -> List[str]:
        ans = []
        for d in range(2, n+1): 
            for x in range(1, d):
                if gcd(x, d) == 1: ans.append(f"{x}/{d}")
        return ans