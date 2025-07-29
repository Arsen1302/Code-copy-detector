class Solution:
    def solution_1092_2_1(self, a: str, b: str) -> bool:
        return self.solution_1092_2_2(a, b) or self.solution_1092_2_2(b, a)
    
    def solution_1092_2_2(self, a, b):
        i = 0
        j = len(a) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        
        return self.solution_1092_2_3(a[:i] + b[i:]) or self.solution_1092_2_3(a[:j + 1] + b[j + 1:])
        
    
    def solution_1092_2_3(self, s):
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True