class Solution:
    def solution_206_1_1(self, s, k):
        c = Counter(s)

        if pattern := "|".join(filter(lambda x: c[x] < k, c)):
            if arr := list(filter(lambda x: len(x) >= k, re.split(pattern, s))):
            
                return max(map(lambda x: self.solution_206_1_1(x, k), arr))
            
            return 0
        
        return len(s)
    
    def solution_206_1_2(self, s: str, k: int) -> int:
        return self.solution_206_1_1(s, k)