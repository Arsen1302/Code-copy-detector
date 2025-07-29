class Solution:
    def solution_1654_4_1(self, k: int, rs1: List[List[int]], cs: List[List[int]]) -> List[List[int]]:
        def solution_1654_4_2(rs):
            adj,ind,q,l = defaultdict(list),{},deque(),[]
            for val in rs:
                adj[val[1]].append(val[0])
                ind[val[0]] = ind.get(val[0],0)+1
            for val in range(1,k+1):
                if ind.get(val,0) == 0:
                    q.append(val)
                    l.append(val)
            while q:
                t = q.popleft()
                for val in adj[t]:
                    ind[val] -= 1
                    if ind[val] == 0:
                        q.append(val)
                        l.append(val)
            return l
        l,l1,dx,dy,ans = solution_1654_4_2(rs1),solution_1654_4_2(cs),{},{},[[0 for i in range(k)]for j in range(k)]
        if len(l) != k or len(l1)!=k:
            return []
        for i in range(k):
            dx[l[i]] = k-1-i
        for j in range(k):
            dy[l1[j]] = k-1-j
        for i in range(1,k+1):
            ans[dx[i]][dy[i]] = i
        return ans