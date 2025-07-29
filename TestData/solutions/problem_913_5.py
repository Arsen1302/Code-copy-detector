class Solution:
    def solution_913_5(self, n: int) -> str:
        if n%2 == 0 and (n//2)%2 != 0:
            return 'a'*(n//2)+'b'*(n//2)
        elif n%2 == 0 and (n//2)%2 == 0:
            return 'a'*((n//2)+1)+'b'*((n//2)-1)
        else:
            return 'a'*n