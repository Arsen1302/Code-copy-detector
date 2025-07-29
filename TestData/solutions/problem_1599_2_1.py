class Solution:
    def solution_1599_2_1(self, n: int, edges: List[List[int]]) -> int:
        
        class dsu:
            def solution_1599_2_2(self,n):
                self.parent=[i for i in range(n)]
                self.size=[1]*n

            def solution_1599_2_3(self,x):
                if x!=self.parent[x]:self.parent[x]=self.solution_1599_2_3(self.parent[x])
                return self.parent[x]
            def solution_1599_2_4(self,u,v):
                u,v=self.solution_1599_2_3(u),self.solution_1599_2_3(v)
                if u!=v:
                    if self.size[u]<self.size[v]:
                        u,v=v,u
                    self.size[u]+=self.size[v]
                    self.size[v]=0
                    self.parent[v]=u
            def solution_1599_2_5(self):
                mp=defaultdict(int)
                for i in range(n):
                    mp[self.solution_1599_2_3(i)]+=1
                return mp
        d=dsu(n)
        for u,v in edges:
            if d.solution_1599_2_3(u)!=d.solution_1599_2_3(v):
                d.solution_1599_2_4(u,v)
        mp=d.solution_1599_2_5()
        ans=0
        for i in mp:
            ans+=(mp[i]*(n-mp[i]))
        return ans//2