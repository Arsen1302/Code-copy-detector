class Solution:
    def solution_467_1(self, S, E):
        L, R, X = 0, 0, 0
        for i, j in zip(S, E):
            L += (j == 'L')
            R += (i == 'R')
            if i == 'R' and L: return False
            if j == 'L' and R: return False
            L -= (i == 'L')
            R -= (j == 'R')
            if L < 0 or R < 0: return False
            X += (i == 'X') - (j == 'X')
        return X == 0