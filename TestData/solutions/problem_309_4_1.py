class Solution:
    def solution_309_4_1(self, s: str, d: List[str]) -> str:
        
        def solution_309_4_2(word): 
            """Return True if word is a subsequence of s."""
            i = 0
            for c in word: 
                while i < len(s) and s[i] != c: i += 1
                if i == len(s): return False 
                i += 1
            return True 
        
        return next((word for word in sorted(d, key=lambda x: (-len(x), x)) if solution_309_4_2(word)), "")