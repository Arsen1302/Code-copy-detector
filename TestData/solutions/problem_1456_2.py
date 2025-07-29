class Solution:
    def solution_1456_2(self, s: str) -> bool:
        appeared_b = False
        for char in s:
            if char == 'b':
                appeared_b = True
            else:
                if appeared_b:
                    return False
        return True