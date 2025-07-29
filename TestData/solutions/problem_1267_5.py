class Solution:
    def solution_1267_5(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0]) # dimensions 
        
        for i in range(m//2): box[i], box[~i] = box[~i], box[i]
        box = [list(x) for x in zip(*box)]
        
        for j in range(m): 
            count = 0 
            for i in range(n): 
                if box[i][j] == "#": 
                    count += 1
                    box[i][j] = "."
                if i+1 == n or box[i+1][j] == "*": 
                    for k in range(count): box[i-k][j] = "#"
                    count = 0
        return box