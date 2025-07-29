class Solution:
    def solution_62_4_1(self, points: List[List[int]]) -> int:
        
        n = len(points)
        if n <= 1:
            return n
        def solution_62_4_2(x1, y1, x2, y2): # (gradient, y-intercept)
            if x1 == x2 and y1 != y2:
      
                return (float('inf'), x1)
            elif x1 != x2 and y1 == y2:
                return (0, y1)
            else:
                gradient = (y2-y1)/(x2-x1)
                intercept =  (x2*y1-x1*y2)/(x2-x1)                                          
                return (gradient, intercept)
            
        info = defaultdict(int)
        for i in range(n-1):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                grad, inter = solution_62_4_2(p1[0], p1[1], p2[0], p2[1])
                info[(grad, inter)] += 1
                
        k = max(info.values())
   
        return int((1 + math.sqrt(1+8*k))/2) ## we want to get v, where k == v*(v-1)//2