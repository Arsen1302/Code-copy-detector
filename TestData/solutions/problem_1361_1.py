class Solution:
    def solution_1361_1(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n): 
                if land[i][j]: # found farmland
                    mini, minj = i, j 
                    maxi, maxj = i, j 
                    stack = [(i, j)]
                    land[i][j] = 0 # mark as visited 
                    while stack: 
                        i, j = stack.pop()
                        for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                            if 0 <= ii < m and 0 <= jj < n and land[ii][jj]: 
                                stack.append((ii, jj))
                                land[ii][jj] = 0 
                                maxi = max(maxi, ii)
                                maxj = max(maxj, jj)
                    ans.append([mini, minj, maxi, maxj])
        return ans