class Solution:
    def solution_532_5_1(self, S: str, T: str) -> bool:
        
        stack_s, stack_t = [], []
        
        # --------------------------------------
        def solution_532_5_2( stk, string ):
            
            for char in string:
                
                if char != '#':
					# push new character into stack
                    stk.append( char )
                    
                elif stk:
                    # pop last charachter from stack, as a result of backspace operation
                    stk.pop() 
                    
            
            return ''.join(stk)
        
        # --------------------------------------
        
        return solution_532_5_2( stack_s, S ) == solution_532_5_2( stack_t, T )