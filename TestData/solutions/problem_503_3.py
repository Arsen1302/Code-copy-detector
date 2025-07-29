class Solution:
    def solution_503_3(self, routes: List[List[int]], source: int, target: int) -> int:
        mp = {}
        for i, route in enumerate(routes): 
            for x in route: 
                mp.setdefault(x, []).append(i)
        
        ans = 0 
        seen = {source}
        queue = [source]
        while queue: 
            newq = []
            for x in queue: 
                if x == target: return ans 
                for i in mp[x]: 
                    for xx in routes[i]: 
                        if xx not in seen: 
                            seen.add(xx)
                            newq.append(xx)
                    routes[i] = []
            ans += 1
            queue = newq
        return -1