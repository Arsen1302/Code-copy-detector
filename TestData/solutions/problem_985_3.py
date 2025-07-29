class Solution:
    def solution_985_3(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxH,maxW=-1,-1
        horizontalCuts.sort()
        hc=[0]+horizontalCuts+[h]
        verticalCuts.sort()
        vc=[0]+verticalCuts+[w]
               
        nH=len(hc)
        for  i in range(1,nH):
            maxH=max(maxH ,hc[i]-hc[i-1] )
        
        nw=len(vc)
        for  i in range(1,nw):
            maxW=max(maxW ,vc[i]-vc[i-1] )
            
        
        return (maxH*maxW % (10**9 + 7))