class Solution:
    def solution_400_2_1(self, s: str) -> bool:
        
        def solution_400_2_2(left, right, changed):            
            while left < right:
                if s[left] != s[right]:
                    if not changed:
                        return solution_400_2_2(left + 1, right, True) or solution_400_2_2(left, right - 1, True)
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
            return True

        return solution_400_2_2(0, len(s) - 1, False)