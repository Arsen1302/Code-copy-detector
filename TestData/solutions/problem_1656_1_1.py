class Solution:
    def solution_1656_1_1(self, n: int) -> bool:
        def solution_1656_1_2(n,b):
            r=""
            while n>0:
                r+=str(n%b)
                n//=b           
            return int(r[-1::-1])
        for i in range(2,n-1):
            if solution_1656_1_2(n,i)!=n:
                return False
        return True