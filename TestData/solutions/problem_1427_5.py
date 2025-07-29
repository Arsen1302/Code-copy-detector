class Solution:
    def solution_1427_5(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        rm=0
        lm=0
        rm=startPos[0]-homePos[0]# number of ups or downs
        lm=startPos[1]-homePos[1] # number of lefts or rights
        ans=0
        if rm<0:#we need to down
            a=startPos[0]
            while rm!=0:
                rm+=1
                ans+=rowCosts[a+1]#add costs according to the row numbers
                a+=1
        elif rm>0:#up
            a=startPos[0]
            while rm!=0:
                rm-=1
                ans+=rowCosts[a-1]
                a-=1
        if lm<0:#left
            a=startPos[1]
            while lm!=0:
                lm+=1
                ans+=colCosts[a+1]
                a+=1
        elif lm>0:#right
            a=startPos[1]
            while lm!=0:
                lm-=1
                ans+=colCosts[a-1]
                a-=1
        return ans