class Solution:
    def solution_403_3(self, a: str, b: str) -> int:
        n = ceil(len(b)/len(a)) # ceiling of len(b)/len(a)
        return next((n+i for i in range(2) if b in (n+i)*a), -1)