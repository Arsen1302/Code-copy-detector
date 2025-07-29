class Solution:
    def solution_224_2_1(self, num1: str, num2: str) -> str:
        def solution_224_2_2(n):
            value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
            result = 0
            for digit in n:
                result = 10 * result + value[digit]

            return result

        ans = solution_224_2_2(num1) + solution_224_2_2(num2)
        return str(ans)