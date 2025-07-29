class Solution:
    def solution_410_4(self, n: int) -> bool:
        if(n<2):
            return True
        n=bin(n)[2:]
        for i in range(1,len(n)):
            if(n[i]==n[i-1]):
                return False
        return True