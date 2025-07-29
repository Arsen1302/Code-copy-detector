class Solution:
    def solution_972_2(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i,j in enumerate(range(len(startTime))):
            if queryTime in range(startTime[i], endTime[j]+1):
                    ans += 1
        
        return ans