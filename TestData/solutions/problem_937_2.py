class Solution:
    def solution_937_2(self, s: str) -> int:          
        found_one = False
        increments = 0
        for num in s[1:][::-1]:
            if num == '1':
                found_one |= True
            elif found_one:
                increments += 1
        
        if found_one:
			increments += 1
            return len(s) + increments
        else:
			return len(s) - 1