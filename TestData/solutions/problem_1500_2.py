class Solution:
    def solution_1500_2(self, s: str, repeatLimit: int) -> str:
        table = Counter(s)
        char_set = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
        sorted_table = []
        for i in range(26,-1,-1):
            if char_set[i] in table:
                sorted_table.append((char_set[i],table[char_set[i]]))

        result = ""
        n = len(sorted_table)
        for i in range(n):
            char, curr_freq = sorted_table[i] # The lexicographically larger character and its frequency
            index_to_take_from = i + 1 # We take from this index the next lexicographically larger character(TEMP) if the repeatLimit for A is exceeded
            while curr_freq > repeatLimit: # Limit exceeded
                result += char*repeatLimit # Add repeatLimit number of character A's
                curr_freq -= repeatLimit # Decrease frequency of character A
                # Now we search for the next lexicographically superior character that can be used once
                while index_to_take_from < n: # Till we run out of characters
                    ch_avail, freq_avail = sorted_table[index_to_take_from]
                    if freq_avail == 0: # If its freq is 0 that means that it was previously used. This is done as we are not removing the character from table if its freq becomes 0. 
                        index_to_take_from += 1 # Check for next lexicographically superior character
                    else:
                        result += ch_avail # If found then add that character 
                        sorted_table[index_to_take_from] = (ch_avail,freq_avail-1) # Update the new characters frequency
                        break
                else:
                    break # We cannot find any lexicographically superior character
            else:
                result += char*curr_freq # If the freq is in limits then just add them
        return result