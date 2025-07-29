class Solution:
    def solution_1508_4(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        retList = [[] for i in range(n) ]
        graph = collections.defaultdict(list)        
        indegree = [0] * n
        topologicalSort = []

        # Build graph and calculate indegree
        for one,two in edges:
            graph[one].append(two)
            indegree[two]+=1
        
        # Until the topological sort is done 
        while len(topologicalSort) != n:
            # Find a source with a indegree of 0
            source = indegree.index(0)
            indegree[source] = -1
            topologicalSort.append(source)

            for node in graph[source]:
                # Add source
                retList[node].append(source)

                # Add parents sources
                retList[node] = list(set(retList[source]).union(set(retList[node])))
                retList[node].sort()

                indegree[node] -=1                       
        
        return retList