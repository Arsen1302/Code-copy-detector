class Solution:
    def solution_390_5(self, n: int, k: int) -> List[int]:
        result = list(range(1,n+1))
        result[0 : k+1 : 2] = list(range(1,(k+2)//2 + 1))
        result[1 : k+1 : 2] = list(range(k+1,(k+2)//2,-1))
        return result