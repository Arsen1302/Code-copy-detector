class Solution:
    def solution_1058_5_1(self,start,end,totalNegitive,firstNegitive,lastNegitive):
        if totalNegitive%2==0:
            return end+1-start
        else:
            if firstNegitive:
                return max(lastNegitive-start,end-firstNegitive)
            else:
                return end-start

    def solution_1058_5_2(self, nums: List[int]) -> int:
        start=0
        totalNegitive=0
        firstNegitive=None
        lastNegitive=None
        result=0
        

        for end,value in enumerate(nums):
            if value<0:
                totalNegitive+=1
                if firstNegitive is None:
                    firstNegitive=end
                lastNegitive=end
            elif value==0:
                if start==end:
                    start+=1
                    continue

                    
                result=max(result,self.solution_1058_5_1(start,end-1,totalNegitive,firstNegitive,lastNegitive))
                
                start=end+1
                lastNegitive=None
                firstNegitive=None
                totalNegitive=0
        result=max(result,self.solution_1058_5_1(start,end,totalNegitive,firstNegitive,lastNegitive))
        return result