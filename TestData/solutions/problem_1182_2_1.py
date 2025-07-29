class Solution:
    def solution_1182_2_1(self, adjacentPairs: List[List[int]]) -> List[int]:
		# create the map 
        adj = collections.defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

		# find the start num
        start = adjacentPairs[0][0]
        for k, v in adj.items():
            if len(v) ==1:
                start = k
                break
				
		# solution_1182_2_2 to connect the graph
        nums=[]
        seen = set()
        def solution_1182_2_2(num):
            seen.add(num)
            for next_num in adj[num]:
                if next_num in seen: continue
                solution_1182_2_2(next_num)
            nums.append(num) 
        solution_1182_2_2(start)
        return nums