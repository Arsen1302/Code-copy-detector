class Solution:
    def solution_1157_5(self, boxTypes: List[List[int]], truckSize: int) -> int:
        c=0
        s=0
        boxTypes=sorted(boxTypes, key=lambda x : -x[1])
        i=0
        while truckSize>0 and i<len(boxTypes):
            truckSize-=boxTypes[i][0]
            if(truckSize>=0):
                s+=boxTypes[i][0]*boxTypes[i][1]
            else:
                c=0-truckSize
                s+=(boxTypes[i][0]-c)*boxTypes[i][1]
            i+=1
        return s