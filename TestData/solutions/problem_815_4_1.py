class Solution:
    def solution_815_4_1(self, n: int, start: int) -> List[int]:
        ans=[]
        def solution_815_4_2(n):
            if n==0:
                ans.append(0)
                return 
            solution_815_4_2(n-1)
            for i in range(len(ans)-1,-1,-1):
                ans.append(ans[i]| 1<<(n-1))
        def solution_815_4_3(ans):
            r=0
            for i in range(len(ans)):
                if ans[i]==start:
                    r=i
                    break 
            return ans[r:]+ans[:r]
        solution_815_4_2(n)        
        ans=solution_815_4_3(ans)
        return ans