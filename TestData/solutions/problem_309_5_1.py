class Solution:
    def solution_309_5_1(self, s: str, d: List[str]) -> str:
        
        def solution_309_5_2(word): 
            """Return True if word is a subsequence of s."""
            i = 0
            for c in s: 
                if i < len(word) and word[i] == c: i += 1
            return i == len(word)
        
        return next((w for w in sorted(d, key=lambda x:(-len(x), x)) if solution_309_5_2(w)), "")