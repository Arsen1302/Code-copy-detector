class Solution:
    def solution_1254_4(self, s: str) -> str:
        res = ""
        for index, char in enumerate(s):
            
            # for each odd number
            if index % 2 != 0 and index != 0:
                
                # get the previous character
                previous_ord = ord(s[index-1])
                
                # get the current character 
                # by summing ordinal of previous and current number
                this = previous_ord + int(char)
                
                # append the chr of the ordinal back to result
                res += chr(this)
            else:
                res += char
        return res