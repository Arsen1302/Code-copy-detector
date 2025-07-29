class Solution:
    def solution_1715_1_1(self, low: int, high: int, zero: int, one: int) -> int:
        def solution_1715_1_2(s,ans):
            if len(s)>=low and len(s)<=high:
                ans+=[s]
            if len(s)>high:
                return 
            solution_1715_1_2(s+"0"*zero,ans)
            solution_1715_1_2(s+"1"*one,ans)
            return
        ans=[]
        solution_1715_1_2("",ans)
        return len(ans)