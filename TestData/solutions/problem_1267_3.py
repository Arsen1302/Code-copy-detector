class Solution:
    def solution_1267_3(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        output = [["" for _ in range(m)] for _ in range(n)]
        
        for row in box:
            prevCount = 0
            for i in range(len(row)):
                if row[i] == "#":
                    prevCount += 1
                    row[i] = "."
                elif row[i] == "*":
                    for j in range(prevCount):
                        row[i-j-1] = "#"
                    prevCount = 0
            
            for j in range(prevCount):
                row[n-j-1] = "#"
        
        for i in range(n):
            for j in range(m):
                output[i][j] = box[m-1-j][i]
        
        return output