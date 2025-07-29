class Solution:
    def solution_547_4(self, bills: List[int]) -> bool:
        _5 = 0
        _10 = 0
        for i in bills:
            if i == 5:
                _5 += 1
            elif i == 10:
                if _5 >= 1:
                    _5 -= 1
                    _10 += 1
                else:
                    return False
            else:
                if _5 >= 1 and _10 >= 1:
                    _5 -= 1
                    _10 -= 1
                elif _5 >= 3:
                    _5 -= 3
                else:
                    return False
        return True