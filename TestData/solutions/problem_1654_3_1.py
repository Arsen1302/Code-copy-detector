class Solution:
    def solution_1654_3_1(self, k: int, rc: List[List[int]], cc: List[List[int]]) -> List[List[int]]:
        def solution_1654_3_2(cond):
            adj=[[] for i in range(k+1)]
            for u,v in cond:
                adj[u].append(v)
            inDegree=[0 for i in range(k+1)]
            topoArray=[]
            q=[]
            for i in range(1,k+1):
                for j in adj[i]:
                    inDegree[j]+=1
            for i in range(1,k+1):
                if inDegree[i]==0:
                    q.append(i)
            while q:
                ele=q.pop(0)
                topoArray.append(ele)
                for it in adj[ele]:
                    inDegree[it]-=1
                    if inDegree[it]==0:
                        q.append(it)
            return topoArray
        t1=solution_1654_3_2(rc)
        t2=solution_1654_3_2(cc)
        if len(t1)<k or len(t2)<k:
            return []
        ans=[[0 for i in range(k)] for i in range(k)]
        hmap=defaultdict(list)
        for ind,x in enumerate(t1):
            hmap[x].append(ind)
        for ind,x in enumerate(t2):
            hmap[x].append(ind)
        for key in hmap.keys():
            x,y=hmap[key]
            ans[x][y]=key
        return ans