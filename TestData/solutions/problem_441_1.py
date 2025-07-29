class Solution:
    def solution_441_1(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # having list with 0`s elements of same lenght as temperature array.
        stack = [] # taking empty stack. 
        for index, temp in enumerate(temperatures): # Traversing through provided list. 
            while stack and temperatures[stack[-1]] < temp: # stack should not be empty and checking previous temp with current temp. 
                # the above while loop and taking stack for saving index is very common practice in monotonic stack questions. Suggestion: understand it properly. 
                prev_temp = stack.pop() # stack.pop() will provide index of prev temp, taking in separate var as we are using it more then on place. 
                result[prev_temp] = index - prev_temp #at the index of prev_temp and i - prev_temp by this we`ll get how many step we moved to have greater temp. 
            stack.append(index) # in case stack is empty we`ll push index in it. 

        return result # returing the list of number of days to wait.