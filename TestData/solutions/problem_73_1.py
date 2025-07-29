class Solution:
    def solution_73_1(self, numerator: int, denominator: int) -> str:
        
        if numerator % denominator == 0: 
			return str(numerator // denominator)
        
        prefix = ''
        if (numerator > 0) != (denominator > 0):
            prefix = '-'
        
        # Operation must be on positive values
        if numerator < 0:
            numerator = - numerator
        if denominator < 0:
            denominator = - denominator

        digit, remainder = divmod(numerator, denominator)
            
        res = prefix + str(digit) + '.' # EVERYTHING BEFORE DECIMAL
        
        table = {}
        suffix = ''
        
        while remainder not in table.keys():
            
            # Store index of the reminder in the table
            table[remainder] = len(suffix)
            
            val, remainder = divmod(remainder*10, denominator)
            
            suffix += str(val)
            
            # No repeating
            if remainder == 0:
                return res + suffix
        
        indexOfRepeatingPart = table[remainder]
        
        decimalTillRepeatingPart = suffix[:indexOfRepeatingPart]
        
        repeatingPart = suffix[indexOfRepeatingPart:]

        return res + decimalTillRepeatingPart + '(' + repeatingPart + ')'

s = Solution()

print(s.solution_73_1(2, 3))