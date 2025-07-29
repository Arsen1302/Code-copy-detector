class Solution:
    def solution_1548_5_1(self, parent: List[int], s: str) -> int:
        n=len(parent)
        adj=[[] for i in range(n)]
        self.ans=0
        for i in range(1,n):
            adj[parent[i]].append(i)   
        def solution_1548_5_2(curr,adj):
            mx,smx=0,0 #max and secondmax value child return to its parent if parent has children>2.
            for it in adj[curr]:
                new=solution_1548_5_2(it,adj)
                if mx<new:
                    smx=mx
                    mx=new
                elif smx<new:
                    smx=new
            self.ans=max(self.ans,mx+smx+1)
            if s[parent[curr]]==s[curr]:
                return 0
            else:
                return mx+1
        solution_1548_5_2(0,adj)
        return self.ans