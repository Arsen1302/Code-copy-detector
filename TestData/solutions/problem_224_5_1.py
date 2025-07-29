class Solution:
    def solution_224_5_1(self, num1: str, num2: str) -> str:
        def solution_224_5_2(s):
            n=0
            for i in s:
                n=n*10+ord(i)-ord('0')
            return n
        
        n,m=solution_224_5_2(num1),solution_224_5_2(num2)
        return str(m+n)