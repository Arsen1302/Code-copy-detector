class Solution:
    def solution_985_2_1(self,distances,lenTotal):
        #Appending first boundary
        distances.append(0)
        #Appending last boundary
        distances.append(lenTotal)
        #Sorting
        distances.sort()
        maxDistancesDiff = 0 
        #Looping to calculate max consecutive distance
        for i in range(1,len(distances)):
            #Getting the difference of two consecutive elements
            currDiff = distances[i] - distances[i-1]
            #Updating max difference value
            maxDistancesDiff = max(maxDistancesDiff,currDiff)       
        return maxDistancesDiff
    
    def solution_985_2_2(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        #Getting max consecutive distance from horizontal distance
        horizontalMaxDiff = self.solution_985_2_1(horizontalCuts,h) 
        #Getting max consecutive distance from vertical distance
        verticalMaxDiff = self.solution_985_2_1(verticalCuts,w) 
        #Returning the result after performing the modulo operation
        return ((horizontalMaxDiff*verticalMaxDiff)%(10**9+7))