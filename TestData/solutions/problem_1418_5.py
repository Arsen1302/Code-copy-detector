class Solution:
    def solution_1418_5(self, tickets: List[int], k: int) -> int:
        
        x=tickets[k]
        answer=0
        for i in range(0,k+1):
            answer+=min(x,tickets[i])
        
        for i in range(k+1,len(tickets)):
            answer+=min(x-1,tickets[i]) 
        
        return answer