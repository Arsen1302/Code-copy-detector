class Solution:
    def solution_696_3(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            if bin(i)[2:] not in s:return 0
        return 1