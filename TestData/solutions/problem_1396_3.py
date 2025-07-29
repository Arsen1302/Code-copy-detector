class Solution:
    def solution_1396_3(self, s: str) -> bool:
        prev = 0
        for token in s.split():
            if token.isnumeric():                
                if (curr := int(token)) <= prev:
                    return False
                prev = curr
        return True