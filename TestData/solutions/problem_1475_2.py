class Solution:
    def solution_1475_2(self, corridor: str) -> int:
        #edge case
        num_S = corridor.count('S')
        if num_S == 0 or num_S % 2 == 1:
            return 0
        
        mod = 10 ** 9 + 7
        curr_s = 0
        res = 1
        spots = 0
        
        for char in corridor:
            curr_s += (char == 'S')
            if curr_s > 0 and curr_s % 2 == 0:
                spots += 1
            else:
                if spots != 0:
                    res = res * spots % mod
                    spots = 0
        
        return res