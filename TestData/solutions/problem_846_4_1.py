class Solution:
    def solution_846_4_1(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = copy.deepcopy(mat)
        
        rsum = 0
        for i in range(m):
            rsum += mat[i][0]
            prefix[i][0] = rsum
            
        csum = 0
        for j in range(n):
            csum += mat[0][j]
            prefix[0][j] = csum
            
        for i in range(1, m):
            for j in range(1, n):
                prefix[i][j] += prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        
        #print(prefix)
        def solution_846_4_2(i, j, mid):
            r, c = i + mid - 1, j + mid - 1
            this = prefix[r][c]
            if j - 1 > -1:
                this -= prefix[r][j - 1]
                
            if i - 1 > -1:
                this -= prefix[i - 1][c]
                
            if i - 1 > -1 and j - 1 > -1:
                this += prefix[i - 1][j - 1]
                
            return this
        
        def solution_846_4_3(mid):
            i, j = 0, 0
            while i <= m - mid:
                j = 0
                while j <= n - mid:
                    this = solution_846_4_2(i, j, mid)
                    if this <= threshold:
                        #print(i, j, mid, this)
                        return True
                    
                    j += 1
                    
                i += 1
                
            return False
            
        
        l, r = 0, threshold
        ans = -1
        
        while l <= r:
            mid = (l + r) // 2
            if solution_846_4_3(mid):
                ans = mid
                l = mid + 1
                
            else:
                r = mid - 1
                
        return ans