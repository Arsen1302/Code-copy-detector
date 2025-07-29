class Solution:
    def solution_957_5_1(self, num: int) -> int:
        
        num_string = str(num)
        
        def solution_957_5_2( src_char: str, dest_char: str, s: str):
        
            return int( s.replace( src_char, dest_char ) )
        
        # -----------------------------------------------------------
        
        # digit replacement for maximum number
        
        max_num = num
        
        for char in num_string:
            if char < '9':
                max_num = solution_957_5_2( char, '9', num_string ) 
                break
        
        # -----------------------------------------------------------
        
        # digit replacement for minimum number
        
        min_num = num
        
        if num_string[0] > '1':
            # leading digit cannot be zero
            min_num = solution_957_5_2( num_string[0], '1', num_string )
        
        else:
            for char in num_string[1:]:
                if char > '1':
                    min_num = solution_957_5_2( char, '0', num_string )
                    break
        
        return max_num - min_num