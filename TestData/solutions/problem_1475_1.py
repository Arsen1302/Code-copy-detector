class Solution:
    def solution_1475_1(self, corridor: str) -> int:
        #edge case
        num_S = corridor.count('S')
        if num_S == 0 or num_S % 2 == 1:
            return 0
        
        mod = 10 ** 9 + 7
        curr_s = 0
        divide_spots = []
        
        for char in corridor:
			curr_s += (char == 'S')
            if curr_s > 0 and curr_s % 2 == 0:
                divide_spots[-1] += 1
            else:
                if not divide_spots or divide_spots[-1] > 0:
                    divide_spots.append(0)
        
        res = 1
        for num in divide_spots[:-1]:
            res = res * num % mod
        return res