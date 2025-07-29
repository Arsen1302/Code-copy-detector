class Solution:
    def solution_1656_2_1(self, n: int) -> bool:
        def solution_1656_2_2(num):
            if num == num[::-1]:
                return True
            return False
        def solution_1656_2_3(num,q):
            res =""
            while num > 0:
                temp = num % q
                res = str(temp) + res
                num //= q
            return res
        for i in range(2,n-1):
            one = solution_1656_2_3(n,i)
            # print(one)
            if not solution_1656_2_2(one):
                return False
        return True