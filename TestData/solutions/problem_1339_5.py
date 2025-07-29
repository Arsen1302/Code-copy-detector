class Solution:
    def solution_1339_5(self, s: str, words: List[str]) -> bool:
        
        x = ''
        for i in words :
            x += i
            if x == s : return True
            if len(x) > len(s) : return False