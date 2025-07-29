class Solution:
    def solution_1399_1_1(self, sentence: str) -> int:
        
        def solution_1399_1_2(word): 
            """Return true if word is valid."""
            seen = False 
            for i, ch in enumerate(word): 
                if ch.isdigit() or ch in "!.," and i != len(word)-1: return False
                elif ch == '-': 
                    if seen or i == 0 or i == len(word)-1 or not word[i+1].isalpha(): return False 
                    seen = True 
            return True 
        
        return sum(solution_1399_1_2(word) for word in sentence.split())