class Solution:
    def solution_393_5(self, num: int) -> int:
       
        # Init
        max_num = num
        
        # Conver num to string
        s = list(str(num))
        n = len(s)
       
        # Loop for each condition
        for i in range(n):
            for j in range(i+1, n):
                
                # Swap i and j
                s[i], s[j] = s[j], s[i]
                
                # Calc max from the string
                max_num = max(max_num, int(''.join(s)))
                
                # Re-Swap i and j, to restore the orginal list
                s[i], s[j] = s[j], s[i]
        
        # return
        return max_num