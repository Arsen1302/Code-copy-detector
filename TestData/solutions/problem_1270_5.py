class Solution:
    def solution_1270_5(self, s):
        ones_counts = [0, 0] # number of ones in odd indecies and even indecies
        for i in range(len(s)):
            if s[i] == '1':
                ones_counts[i%2] += 1
        num_ones = ones_counts[0] + ones_counts[1]
        num_zeros = len(s) - num_ones
        
        if num_zeros - num_ones > 1 or num_zeros - num_ones < -1:
            return -1
        elif num_zeros - num_ones == 1: # num zeroes are num ones + 1
            #return num_ones - ones_counts[1]
            return ones_counts[0]
        elif num_ones - num_zeros == 1:
            return ones_counts[1]
        else:
            return min(ones_counts[0], ones_counts[1])