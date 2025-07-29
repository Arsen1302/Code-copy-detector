class Solution:
    def solution_430_4(self, source: List[str]) -> List[str]:
        
        '''
        is_block shows if we're in a block comment or not
        Iterate over current line and detect line comments or start/end of block comments.
        End line early for a line comment, update is_block for block start/end and continue
        Only create new res_line if we reach the end of a line and is_block is false. 
            This accounts for test cases like ["a/*comment", "line", "more_comment*/b"] -> ["ab"].
        '''
        
        # define vars
        is_block = False
        res_line = []
        result = []
        
        # iterate over lines 
        for source_line in source:
        
            # iterate over characters in line, look ahead for comment denoters
            i = 0
            while i < len(source_line):
            
                char = source_line[i]

                # is this the start of a line comment?
                if not is_block and source_line[i:i+2] == '//':
                    i = len(source_line) # skip to end

                # is this the start of a block comment?
                elif not is_block and source_line[i:i+2] == '/*':
                    is_block = True
                    i += 2

                # is this the end of a block comment?
                elif is_block and source_line[i:i+2] == '*/':
                    is_block = False
                    i += 2
                    
                # we're in a block comment, skip the char
                elif is_block:
                    i += 1
                    
                # we can add the char
                else:
                    res_line.append(char)
                    i += 1
                    
            # if not is_block, add to result and reset, filter empty lines
            if res_line and not is_block:
                result.append(''.join(res_line))
                res_line = []
                
        return result