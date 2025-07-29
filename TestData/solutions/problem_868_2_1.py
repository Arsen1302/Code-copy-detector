class Solution:
    def solution_868_2_1(self, n: int) -> List[int]:
        def solution_868_2_2(num):
            while num>0:
                if num%10==0:
                    return False
                num//=10
            return True
        for i in range(1,n):
            t=n-i
            if solution_868_2_2(t) and solution_868_2_2(i):
                return [i,t]