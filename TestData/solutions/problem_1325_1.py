class Solution:
    def solution_1325_1(self, segments: List[List[int]]) -> List[List[int]]:
		# via this mapping, we can easily know which coordinates should be took into consideration.
        mapping = defaultdict(int)
        for s, e, c in segments:
            mapping[s] += c
            mapping[e] -= c
        
        res = []
        prev, color = None, 0
        for now in sorted(mapping):
            if color: # if color == 0, it means this part isn't painted.
                res.append((prev, now, color))
            
            color += mapping[now]
            prev = now
            
        return res