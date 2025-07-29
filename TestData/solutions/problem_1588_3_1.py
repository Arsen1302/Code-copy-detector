class Solution:
    def solution_1588_3_1(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if len(s) < len(sub): 
            return False 
        maps = defaultdict(set)
        for u, v in mappings:
            maps[u].add(v)
        
        def solution_1588_3_2(s1):
            for c1, c2 in zip(s1, sub): 
                if c1 != c2 and c1 not in maps[c2]: 
                    return False 
            return True 
        
        for i in range(len(s) - len(sub) + 1):
            if solution_1588_3_2(s[i:i+len(sub)]):
                return True

        return False