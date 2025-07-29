class Solution:
    def solution_309_3_1(self, s: str, d: List[str]) -> str:
        
        def solution_309_3_2(word): 
            """Return True if word matches a subsequence of s."""
            ss = iter(s)
            return all(c in ss for c in word)
        
        ans = ""
        for w in d: 
            if solution_309_3_2(w) and (len(w) > len(ans) or len(w) == len(ans) and w < ans): ans = w
        return ans