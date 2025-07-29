class Solution(object):
    def solution_430_5(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        
        # initialize some variables to save lines and valid characters
        result = []
        current_line = ""
        
        # initialize some state variables
        in_block = False
        in_line = False
        skip_next = False
        
        for line in source:
            
            # in a new line we will never skip the first character
            skip_next = False
            
            # a new line can never be part of an inline comment
            in_line = False
            
            for index, character in enumerate(line):
                
                # ----------------------------------------------------------------
                # Guard clauses that will always skip the character, if we are in
                # a comment or notified the loop to skip the next
                # -----------------------------------------------------------------
                
                # guard clause whether we want to skip the current character
                if skip_next:
                    
                    # reset the boolean in case we skip
                    skip_next = False
                    continue
                
                # guard clause whether we are in an in line comment
                # this comment can only be ended by a new line so we do not need
                # to check the current character
                if in_line:
                    continue
                    
                # guard clause whether we are in a block comment
                if in_block:
                    
                    # since the block comment can be ended, we need to check whether we find
                    # our ending symbol
                    # line[index:index+2] slicing works also at the end of a line
                    # (even if index+2 is out of scope)
                    if line[index:index+2] == '*/':
                        
                        # in case we found the end of the block comment we switch the bool to false
                        # and we need to skip the next character
                        # Our current character (line[index]) is '*' and the next is '/' which we skip
                        in_block = False
                        skip_next = True
                        continue
                    else:
                        
                        # we are still in block comment and therefore can continue
                        continue
                
                
                # ----------------------------------------------------------------
                # After all guard clauses passed, we are not in a comment and
                # we need to check the current character whether it starts one
                # -----------------------------------------------------------------
                
                # check whether block comment begins
                # slicing of list works even if index+2 is out of scope
                if line[index:index+2] == '/*':
                    
                    # switch the comment boolean and 
                    # tell our loop we need to skip the next character
                    # since it will be a '*'
                    in_block = True
                    skip_next = True
                    continue
                
                # check whether in line comment starts
                # slicing works also at end of line
                if line[index:index+2] == '//':
                    
                    # we switch the boolean and  skip the next character as it will be
                    # '/'
                    in_line = True
                    skip_next = True
                    continue
                
                # ----------------------------------------------------------------
                # Now that all checks have passed we found
                # a character that is part of the code
                # -----------------------------------------------------------------
                
                
                # append our character to the current line
                current_line += character
            
            
            # we will append the current line to our result (finalize a line in the output)
            # a) if we are not in a block comment that hasn't ended
            # b) and the current line has characters in it
            if not in_block and current_line:
                
                # append the line and reset the current line
                result.append(current_line)
                current_line = ""
                
        return result