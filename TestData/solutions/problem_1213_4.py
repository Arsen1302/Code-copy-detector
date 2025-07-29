class Solution:
    def solution_1213_4(self, s: str) -> bool:
        
        f = False
        for i in s:
            if i == '1':
                if not f:
                    continue
                else:
                    return False
            else:
                f = True
        return True