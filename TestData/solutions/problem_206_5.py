class Solution:
    def solution_206_5(self, s: str, k: int) -> int:
        if not s: return 0 # edge case 
        
        freq = {} # frequency table 
        for c in s: freq[c] = 1 + freq.get(c, 0)
            
        if min(freq.values()) < k: 
            m = min(freq, key=freq.get)
            return max(self.solution_206_5(ss, k) for ss in s.split(m))
        return len(s)