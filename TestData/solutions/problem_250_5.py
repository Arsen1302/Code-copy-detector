class Solution:
    def solution_250_5(self, s: str) -> str:
        character_to_index        = {}
        characters_with_frequency = []
        
        
        for character in s:
            if ( character not in character_to_index ):
                character_to_index[character] = len(characters_with_frequency)
                characters_with_frequency.append([character, 1])
            else:
                index                                = character_to_index[character]
                characters_with_frequency[index][1] += 1
                frequency                            = characters_with_frequency[index][1]
                
                
                if ( index > 0 and characters_with_frequency[index  - 1][1] <= frequency ):
                    while ( index > 0 and characters_with_frequency[index  - 1][1] <= frequency ):
                        character_to_index[characters_with_frequency[index - 1][0]] = index
                        characters_with_frequency[index]                            = characters_with_frequency[index - 1]
                        index                                                      -= 1 

                    character_to_index[character]    = index
                    characters_with_frequency[index] = [character, frequency] 
     
        return "".join([character * frequency for character, frequency in characters_with_frequency])