class Solution:
    def solution_923_3_1(self,n,dict1):
        if n in dict1:
            return dict1[n]

        if n%2 == 0:
            dict1[n] = 1 + self.solution_923_3_1(n//2,dict1)
        else:
            dict1[n] = 1 + self.solution_923_3_1(3*n+1,dict1)

        return dict1[n]

    def solution_923_3_2(self, lo, hi, k):
        ans = [i for i in range(lo,hi+1)]
        ans.sort(key = lambda x: self.solution_923_3_1(x,{1:0}))
        return ans[k-1]