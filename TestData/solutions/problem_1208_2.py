class Solution:
    def solution_1208_2(self, cars: List[List[int]]) -> List[float]:
        n=len(cars)
        ans=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and cars[i][1]<=cars[stack[-1]][1]:
                stack.pop()
            while stack:
                collisionTime=(cars[stack[-1]][0]-cars[i][0])/(cars[i][1]-cars[stack[-1]][1])
                if collisionTime<=ans[stack[-1]] or ans[stack[-1]]==-1:
                    ans[i]=collisionTime
                    break
                stack.pop()
            stack.append(i)
        return ans