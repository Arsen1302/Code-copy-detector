class Solution:
    def solution_1724_3_1(self, roads: List[List[int]], seats: int) -> int:
        m = defaultdict(list)
        
        for a,b in roads:
            m[a].append(b)
            m[b].append(a)
            
        ans = [0]
        
        def solution_1724_3_2(node, prev):
		
            people = 1
            
            for i in m[node]:
			
                if i==prev:
                    continue
                
                people+=solution_1724_3_2(i, node)
                
            if node!=0:
                ans[0]+=math.ceil(people/seats)
                
            return people
			
        solution_1724_3_2(0, None)
		
        return ans[0]