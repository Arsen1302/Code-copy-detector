class Solution:
    def solution_1157_4(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans=0
        i=0     #To traverse array
        
        #Sort according to decreasing values of numberOfBoxes
        boxTypes.sort(key=lambda x:(-x[1]))
        
        n=len(boxTypes)
        while(truckSize!=0 and i<n):
            print(truckSize)
            if truckSize > boxTypes[i][0]:
                ans += boxTypes[i][0]*boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i+=1
            
            elif truckSize <= boxTypes[i][0]:
                ans += truckSize*boxTypes[i][1]
                return ans
        
        return ans