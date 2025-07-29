class Solution:
    def solution_1402_4(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree=[0]*n
        adj=[[] for i in range(n)]
        for i,j in relations:
            adj[i-1].append(j-1)
            indegree[j-1]+=1
        preReq_time=defaultdict(int)
        q=[(time[x],x) for x in range(n) if indegree[x]==0]
        heapify(q)
        cnt=0
        while q:
            t,course=heappop(q)
            cnt+=1
            if cnt==n:
                return t
            for it in adj[course]:
                indegree[it]-=1
                preReq_time[it]=max(preReq_time[it],t)
                if indegree[it]==0:
                    heappush(q,(preReq_time[it]+time[it],it))