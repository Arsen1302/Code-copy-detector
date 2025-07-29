class Solution:
    def solution_1574_3(self, a: List[List[int]]) -> int:
        if len(a)<=1:
            return 0
        a.sort()
        ans=1
        for i in range(2,len(a)):
            
            if ((a[i-1][1]-a[i-2][1])*(a[i][0]-a[i-1][0]))!=((a[i][1]-a[i-1][1])*(a[i-1][0]-a[i-2][0])):
                ans+=1
                
        return ans