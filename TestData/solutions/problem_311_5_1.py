class Solution:
    def solution_311_5_1(self, n: int) -> int:
        res=[0]
        def solution_311_5_2(i,arr):
            if i==n+1:
                res[0]+=1
                return 
            m=len(arr)
            for j in range(m):
                e=arr.pop(0)
                if (not i%e) or (not e%i):
                    solution_311_5_2(i+1,arr)
                arr.append(e)
        solution_311_5_2(1,[i for i in range(1,n+1)])
        return res[0]