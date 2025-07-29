class Solution:
    def solution_1586_5(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        lower = upper = digit = special = False
        
        prev = ""
        for char in password:
            if char == prev:
                return False
            if char.islower():
                lower = True
            elif char.isupper():
                upper = True
            elif char.isdigit():
                digit = True
            else:
                special = True
            prev = char
        
        return lower and upper and digit and special