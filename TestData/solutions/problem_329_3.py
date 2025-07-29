class Solution:
    def solution_329_3(self, n: int) -> int:
        ss = list(str(n))
        for i in reversed(range(len(ss)-1)):
            if ss[i] < ss[i+1]: break 
        else: return -1 # no break encounter 
        
        for ii in reversed(range(i+1, len(ss))):
            if ss[i] < ss[ii]: break 
        ss[i], ss[ii] = ss[ii], ss[i] # swap 

        i, j = i+1, len(ss)-1 # reverse 
        while i < j: 
            ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        ans = int("".join(ss))
        return ans if ans < 2**31 else -1