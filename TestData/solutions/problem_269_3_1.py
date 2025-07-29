class Solution:
    def solution_269_3_1(self, houses: List[int], heaters: List[int]) -> int:
       
        heaters.sort() # so that we can use binary search
        result = float("-inf")
        for house in houses:
            distanceToNearestHeater = self.solution_269_3_2(house, heaters)
            result = max(result, distanceToNearestHeater)
        return result
            
    def solution_269_3_2(self, house, heaters):
        if len(heaters) == 1: # if only 1 heater present, then its obvious
            return abs(house - heaters[0])
        
        left = 0
        right = len(heaters) - 1
        justGreater, justSmaller = -1, -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if house == heaters[mid]: # if heater at position of house, 0 distance
                return 0
            
            if house < heaters[mid]:
                justGreater = heaters[mid]
                right = mid - 1
            else:
                justSmaller = heaters[mid]
                left = mid + 1
                
        # if we have 2 heaters available, return min of, distance from house to those heaters.
        if justGreater != -1 and justSmaller != -1: 
            return min(abs(house - justGreater), abs(house - justSmaller))
        
        # if we dont have a heater towards right, return distance from house to nearest left heater
        if justGreater == -1:
            return abs(house - justSmaller)
        # if we dont have a heater towards left, return distance from house to nearest right heater
        else:
            return abs(house - justGreater)