class Solution:
    def solution_1179_5(self, matrix: List[List[int]], k: int) -> int:
        
        res = []                                                                
        prefix_sum = [[0]*(len(matrix[0])+1) for _ in range(0,len(matrix)+1)]   #initialize prefix sum matrix
        
        # for each index (i,j) in matrix, calculate XOR of prefix_sum[i-1][j] and matrix[i][j]
        # then XOR the result with XOR of all values from matrix[i][0] to matrix[i][j-1] 
        for i in range(1,len(matrix)+1):
            XOR_value = 0                                                       #initialize XOR value for row i of matrix
            for j in range(1,len(matrix[0])+1):
                XOR_value ^= matrix[i-1][j-1]                                   #XOR with value at index i,j of matrix (as loops start from 1, we use indices i-1 and j-1)
                prefix_sum[i][j] = XOR_value^prefix_sum[i-1][j]                 #update current index of prefix sum by XORing the current XOR value with the prefix sum at the upper cell
                res.append(prefix_sum[i][j])                                    #store this resultant XOR at res
                    
        return sorted(res)[-k]                                                  #need k'th largest element, so sort it and get the value at the (k-1)'th index from the right