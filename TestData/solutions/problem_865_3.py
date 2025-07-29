class Solution:
    def solution_865_3(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
		
		# Calculate the prefix sum
        prefix = mat[:][:]  # essentially copies the entire array
        for i in range(m):
            for j in range(n):
                prefix[i][j] += (prefix[i-1][j] if i > 0 else 0) + \          # add prefix sum of (i-1, j) if it exists
                                (prefix[i][j-1] if j > 0 else 0) - \          # add prefix sum of (i, j-1) if it exists
                                (prefix[i-1][j-1] if i > 0 and j > 0 else 0)  # subtract prefix sum of (i-1, j-1) if it exists
		
		# Calculate the block sum from the prefix sum
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = prefix[min(i+k, m-1)][min(j+k, n-1)] + \                  # S(D), bounded by m x n
                               (prefix[i-k-1][j-k-1] if i-k > 0 and j-k > 0 else 0) - \  # S(A), if it exists
                               (prefix[i-k-1][min(j+k, n-1)] if i-k > 0 else 0) - \      # S(B), if it exists
                               (prefix[min(i+k, m-1)][j-k-1] if j-k > 0 else 0)          # S(C), if it exists
        return result
		# we could technically shorten the block sum calculation into one line of code, but that is super unreadable