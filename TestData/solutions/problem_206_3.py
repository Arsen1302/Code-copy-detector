class Solution:
    def solution_206_3(self, s: str, k: int) -> int:
        
        if len(s)==0:
            return 0
        
        cnt = collections.Counter(s)
        
        for i in cnt:
            if cnt[i] < k:
                # print(s.split(i))
                return max(self.solution_206_3(p,k) for p in s.split(i))
                
        return len(s)