class Solution:
    def solution_1367_5(self, rectangles: List[List[int]]) -> int:
        
        hashmap , pairs = {} , 0
        
        for i in range(len(rectangles)):
            
            key = rectangles[i][0] / rectangles[i][1]
            
            if key in hashmap:
                
                pairs += hashmap[key]
                
                hashmap[key] += 1
                
            else:
                
                hashmap[key] = 1
            
        return pairs