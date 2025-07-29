class Solution:
def solution_1322_4_1(self, points: List[List[int]]) -> int:
    
    m = len(points)
    n = len(points[0])
    
    if m==1:
        return max(points[0])
    
    if n==1:
        s=0
        for j in range(m):
            s+=points[j][0]
        return s
    
    def solution_1322_4_2(row):
        left = [ele for ele in row]
        for i in range(1,len(left)):
            left[i] = max(left[i], left[i-1]-1)
        return left
    
    def solution_1322_4_3(row):
        right = [ele for ele in row]
        for i in range(len(row)-2,-1,-1):
            right[i] = max(right[i],right[i+1]-1)
        return right
    
    pre  = points[0]
    for i in range(1,m):
        left = solution_1322_4_2(pre)
        right= solution_1322_4_3(pre)
        curr = [0 for _ in range(n)]
        for j in range(n):
            curr[j] = points[i][j]+max(left[j],right[j])    
        pre = curr[:]
                    
    return max(pre)