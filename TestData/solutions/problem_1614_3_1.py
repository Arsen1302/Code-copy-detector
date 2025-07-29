class Solution:
    def solution_1614_3_1(self, amount: List[int]) -> int:
        mp={}
        def solution_1614_3_2(x1,x2,x3):
            if x1<=0 or x2<=0 or x3<=0:
                return max(x1,x2,x3)
            if (x1,x2,x3) in mp :
                return mp[(x1,x2,x3)]
            mp[(x1,x2,x3)]=1+min(solution_1614_3_2(x1-1,x2-1,x3),solution_1614_3_2(x1,x2-1,x3-1),solution_1614_3_2(x1-1,x2,x3-1))
            return mp[(x1,x2,x3)]
        return solution_1614_3_2(amount[0],amount[1],amount[2])