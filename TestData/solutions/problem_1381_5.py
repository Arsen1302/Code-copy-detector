class Solution:
    def solution_1381_5(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if(len(original)!= (m*n)):
            return []
        matrix = [[0]*n for i in range(m)]
        index=0
        for rows in range(m):
            for cols in range(n):
                matrix[rows][cols]= original[index]
                index+=1
        return matrix