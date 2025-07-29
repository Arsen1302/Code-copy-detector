class Solution(object):
    def solution_1381_4(self,original, m, n):
	
        result = []

        if len(original)==m*n:
            for row in range(m):
                result.append(original[n*row:n*row+n])

        return result