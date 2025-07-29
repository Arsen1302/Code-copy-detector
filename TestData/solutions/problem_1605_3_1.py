class Solution:
    def solution_1605_3_1(self, nums: List[int], edges: List[List[int]]) -> int:
        s,n=0,len(nums)
        for x in nums:
            s^=x
        es=[[] for _ in range(n)]
        for a,b in edges:
            es[a].append(b)
            es[b].append(a)
        def solution_1605_3_2(a,b,c):
            return max(a,b,c)-min(a,b,c)
        def solution_1605_3_3(x,par=-1):
            S,m,p=[],10**9,nums[x]
            for y in es[x]:
                if y!=par:
                    t,u,v=solution_1605_3_3(y,x)
                    m=min(m,u,min(solution_1605_3_2(s^v,v^k,k) for k in t) if t else u)
                    t.add(v)
                    S.append(t)
                    p^=v
            r=set()
            for t in S:
                r|=t
            for i in range(len(S)):
                for j in range(i+1,len(S)):
                    m=min(m,min(solution_1605_3_2(s^k^l,k,l) for k in S[i] for l in S[j]))
            return r,m,p
        return solution_1605_3_3(0)[1]