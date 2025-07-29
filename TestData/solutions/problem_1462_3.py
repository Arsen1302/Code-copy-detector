class Solution:
    def solution_1462_3(self, words: List[str]) -> int:
        c = collections.Counter(words)
        
        res = 0
        mid = 0
        
        for key in c:
            mirror = key[::-1]
            
            if key == mirror:
                res += 2 * (c[key] // 2)
                mid |= c[key] % 2
            else:
                if c[mirror] != 0:
                    res += min(c[key], c[mirror])

        return res * 2 + (2 if mid else 0)