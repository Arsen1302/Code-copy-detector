class Solution:
    def solution_1450_4(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
			
        open_count, options, options_borrowed = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == "0":
                if open_count:
                    open_count -= 1
                    options_borrowed += 1
                else:
                    options += 1
                continue
                
            if s[i] == "(":
                open_count += 1
                continue
                
            if open_count:
                open_count -= 1
            elif options_borrowed:
                options_borrowed -= 1
                options += 1
            elif options:
                options -= 1
            else:
                return False
                
        if open_count:
            return False
        return True