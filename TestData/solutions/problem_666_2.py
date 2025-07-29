class Solution:
    def solution_666_2(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        s,e = 0,1
        i,j = 0,0
        
        while i < len(firstList) and j < len(secondList):
            a = firstList[i] # fetching the interval
            b = secondList[j] # fetching the interval
            # checking for the overlapping 
            if b[s] <= a[e] and b[e] >= a[s]:
                # fetching the intersection point
                intersectionPoint = [max(a[s],b[s]),min(a[e],b[e])]
                res.append(intersectionPoint) # appending intersectionPoint into result list
                
            if a[e] > b[e]:
                j += 1
            else:
                i += 1
        return res