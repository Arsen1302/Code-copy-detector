class Solution:
    def solution_77_5(self, columnTitle: str) -> int:
	
		# Use dictionary to map alphabets A to Z one-on-one to integer 1 to 26:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = range(1,27)
        alpha_to_nums = {alphabet[i]: nums[i] for i in range(len(alphabet))}
		
		# Express the formula above in a simple for loop, iterating from the last digit:
        column_number = 0
        for pos, letter in enumerate (reversed(columnTitle)):
            column_number +=  26**(pos) * alpha_to_nums[letter] 
			
        return column_number