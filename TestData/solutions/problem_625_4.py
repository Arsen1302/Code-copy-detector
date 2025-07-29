class Solution:
    def solution_625_4(self, strs: List[str]) -> int:
        C = len(strs[0])
        res = 0
        
        for col in range(C):
            unsorted_flag = False
                
            for si in range(1, len(strs)):
                if strs[si][col] < strs[si-1][col]:
                    unsorted_flag = True
                    
            if unsorted_flag:
                res += 1 # this col is unsorted
                
        return res