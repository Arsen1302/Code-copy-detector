class Solution:
    def solution_504_1_1(self, s: str) -> List[str]:
        s = s.strip("(").strip(")")
        
        def solution_504_1_2(s): 
            """Return valid numbers from s."""
            if len(s) == 1: return [s]
            if s.startswith("0") and s.endswith("0"): return []
            if s.startswith("0"): return [s[:1] + "." + s[1:]]
            if s.endswith("0"): return [s]
            return [s[:i] + "." + s[i:] for i in range(1, len(s))] + [s]
        
        ans = []
        for i in range(1, len(s)): 
            for x in solution_504_1_2(s[:i]):
                for y in solution_504_1_2(s[i:]): 
                    ans.append(f"({x}, {y})")
        return ans