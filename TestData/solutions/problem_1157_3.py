class Solution:
    def solution_1157_3(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1] , reverse=True)
                
        count = 0
        
        k = 0
        
        for i , j in boxTypes:
            if(truckSize < i):
                break
            
            count += i * j
            
            truckSize -= i
            
            k += 1
        
        try:
            return count + (truckSize * boxTypes[k][1])
        except:
            return count