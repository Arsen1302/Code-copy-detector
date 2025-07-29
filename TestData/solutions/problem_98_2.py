class Solution:
    def solution_98_2(self, numCourses: int, pr: List[List[int]]) -> List[int]:
	
        # Build adjacency list
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            
        # TopoSort
        topo = list()
        vis = set()
        processed = set()
        for node in range(numCourses):
            if node in vis:
                continue
                
            st = [node]
            while st:
                cur = st[-1]
                vis.add(cur)
                
                if cur in processed:
                    st.pop()
                    continue
                
				for ch in adj[cur]:
					if not ch in vis:
						st.append(ch)
                    
                if cur == st[-1]:
                    topo.append(st.pop())
                    processed.add(cur)

        # Result
        res = []
        i = 0
        pos = dict()
        while topo:
            node = topo.pop()
            pos[node] = i
            i += 1
            res.append(node)
        
        # Check for cycles
        for parent, children in adj.items():
            for child in children:
                if pos[parent] > pos[child]:
                    return []
        
        return res