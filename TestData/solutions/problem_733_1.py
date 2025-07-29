class Solution:
def solution_733_1(self, matrix: List[List[int]]) -> int:
    
    dic = defaultdict(int)
    for row in matrix:
        local=[]
        for c in row:
            local.append(c^row[0])
        dic[tuple(local)]+=1
    
    return max(dic.values())