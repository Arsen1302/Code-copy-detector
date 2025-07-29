class Solution:
    def solution_224_3_1(self, num1: str, num2: str) -> str:
        s = {str(i):i for i in range(10)}
        
        def solution_224_3_2(num: str, ret: int = 0) -> int:
            for ch in num: ret = ret * 10 + s[ch]
            return ret
        
        return str(solution_224_3_2(num1) + solution_224_3_2(num2))