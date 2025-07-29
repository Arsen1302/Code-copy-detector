class Solution:

    def solution_113_5(self, s: str) -> int:
        # Edge cases
        if len(s) == 0: # empty string
            return 0
        
        # remove all spaces
        s = s.replace(" ", "")
        
		# Initialization 
        curr_number = prev_number = result = 0 
        operation = "+" # intitialize the current operation to be "addition"
        
        i = 0 # initialize i
        while i < len(s): # len(s) is the length of the string
            char = s[i] # parsing ghe current currecter
            # if the character is digit
            if char.isdigit(): # current character is digit
                while i < len(s) and s[i].isdigit():
                    curr_number = curr_number * 10 + int(s[i]) # forming the number (112 for example)
                    i += 1 # increment i by 1 if s[i] is still a digit
                i -= 1 # decrement i by 1 to go back to the location immediately before the current operation
                
                if operation == "+": 
                    result += curr_number # add the curr_number to the result
                    prev_number = curr_number # update the previous number
                    
                elif operation == "-": 
                    result -= curr_number # subtract the curr_number from the result
                    prev_number = -curr_number # update the previous number
                    
                elif operation == "*":
                    result -= prev_number # subtract the previous number first
                    result += prev_number * curr_number # add the result of multiplication
                    prev_number = prev_number * curr_number # update the previous number
                    
                elif operation == "/":
                    result -= prev_number # subtract the previous number first
                    result += int(prev_number/curr_number) # add the result of division
                    prev_number = int(prev_number/curr_number) # update the previous number
                    
                curr_number = 0 # reset the current number
            # if the character is an operation
            else:
                operation = char
                
            i += 1 # increment i by 1
        return result