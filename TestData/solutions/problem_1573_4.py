class Solution:
    def solution_1573_4(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        empty = []
        
        for i in range(len(rocks)):
            empty.append(capacity[i]-rocks[i])
            
        empty.sort()
        
        bags = 0
        
        for i in range(len(empty)):
            additionalRocks -= empty[i]
            
            if additionalRocks < 0:
                return bags
            
            bags += 1
            
        return bags