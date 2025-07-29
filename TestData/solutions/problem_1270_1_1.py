class Solution:
    def solution_1270_1_1(self, s: str) -> int:
        ones = s.count("1")
        zeros = len(s) - ones 
        if abs(ones - zeros) > 1: return -1 # impossible
        
        def solution_1270_1_2(x): 
            """Return number of swaps if string starts with x."""
            ans = 0 
            for c in s: 
                if c != x: ans += 1
                x = "1" if x == "0" else "0"
            return ans//2
        
        if ones > zeros: return solution_1270_1_2("1")
        elif ones < zeros: return solution_1270_1_2("0")
        else: return min(solution_1270_1_2("0"), solution_1270_1_2("1"))