class Solution:
    def solution_843_3(self, arr: List[List[int]]) -> int:
        for i in range(1, len(arr)): 
            #find 1st &amp; 2nd mininum
            m1 = m2 = float("inf")
            for x in arr[i-1]: 
                if x < m1: m1, m2 = x, m1
                elif x < m2: m2 = x
                    
            #update min falling path sum as of row i 
            for j in range(len(arr[0])): 
                arr[i][j] += (m1 if arr[i-1][j] != m1 else m2)
                    
        return min(arr[-1])