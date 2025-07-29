class Solution:
    def solution_577_1_1(self, words: List[str], pattern: str) -> List[str]:
        
        def solution_577_1_2( s ):
            
            # dictionary
            # key   : character
            # value : serial number in string type
            char_index_dict = dict()
            
            # given each unique character a serial number
            for character in s:
                
                if character not in char_index_dict:
                    char_index_dict[character] = str( len(char_index_dict) )
            
            
            # gererate corresponding pattern string
            return ''.join( map(char_index_dict.get, s) )

        #--------------------------------------------------------    
            
        pattern_string = solution_577_1_2(pattern)
        
        return [ word for word in words if solution_577_1_2(word) == pattern_string ]