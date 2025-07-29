class Solution:
    def solution_1696_2_1(self, num: int) -> bool:
        def solution_1696_2_2(a,b):
            return b==int(str(a)[-1::-1])
        t=num
        i=0
        while i<=t:
            if i+t==num:
                if solution_1696_2_2(t,i):
                    return True
            i+=1
            t-=1
        return False