class Solution:
    def solution_1184_2(self, s: str) -> bool:
        mp = defaultdict(set)
        for i in range(2*len(s)-1): 
            lo, hi = i//2, (i+1)//2
            while 0 <= lo <= hi < len(s) and s[lo] == s[hi]: 
                mp[lo].add(hi)
                lo, hi = lo-1, hi+1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if i-1 in mp[0] and j-1 in mp[i] and len(s)-1 in mp[j]: return True
        return False