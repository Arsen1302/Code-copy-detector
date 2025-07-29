class Solution:
    def solution_536_1(self, S: str, shifts: List[int]) -> str:
        
        final_shift = list(accumulate(shifts[::-1]))[::-1]
        
        s_list = list(S)
        
        for x in range(len(s_list)):
            midval = ord(s_list[x]) + final_shift[x]%26
            if midval > 122:
                midval = midval - 26
            
            s_list[x] = chr(midval)
        
        return ''.join(s_list)