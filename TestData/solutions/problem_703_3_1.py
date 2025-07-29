class Solution:
    def solution_703_3_1(self, queries: List[str], pattern: str) -> List[bool]:
        
        def solution_703_3_2(query):
            """Return True if query matches pattern."""
            i = 0 
            for x in query: 
                if i < len(pattern) and x == pattern[i]: i += 1
                elif x.isupper(): return False 
            return i == len(pattern)
        
        return [solution_703_3_2(query) for query in queries]