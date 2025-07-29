class Solution:
    def solution_309_2_1(self, s: str, d: List[str]) -> str:
        
        def solution_309_2_2(word): 
            """Return True if word matches a subsequence of s."""
            ss = iter(s)
            return all(c in ss for c in word)
        
        return next((w for w in sorted(d, key=lambda x: (-len(x), x)) if solution_309_2_2(w)), "")