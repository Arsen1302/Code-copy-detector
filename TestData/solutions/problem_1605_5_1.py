class Solution:
    def solution_1605_5_1(self, nums: List[int], edges: List[List[int]]) -> int:
        hmap=defaultdict(int)
        pc,par=[],[]
        n=len(nums)
        childs=[[False for i in range(n)] for j in range(n)]
        graph=[[] for i in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        vis=set()
        def solution_1605_5_2(curr):
            for p in par:childs[p][curr]=True
            par.append(curr)
            currXor=nums[curr]
            for it in graph[curr]:
                if it not in vis:
                    vis.add(it)
                    pc.append((curr,it))
                    val=solution_1605_5_2(it)
                    currXor^=val
            par.pop()
            hmap[curr]=currXor
            return currXor
        vis.add(0)
        solution_1605_5_2(0)
        m=len(pc)
        ans=float('inf')
        for a in range(m):
            for b in range(a+1,m):
                f,s=pc[a][1],pc[b][1]
                xf,xs,xp=hmap[f],hmap[s],hmap[0]
                if childs[f][s]:
                    xp^=xf
                    xf^=xs
                else:
                    xp^=xf
                    xp^=xs
                ans=min(ans,max(xp,xf,xs)-min(xp,xf,xs))
        return ans