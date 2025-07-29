class Solution:
    def solution_192_4(self, matrix: List[List[int]], k: int) -> int:
        
        r = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(r, -matrix[i][j])
                while len(r) > k:
                    print(heappop(r))
                    
        return -heappop(r)