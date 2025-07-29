class Solution:
    def solution_996_4_1(self, bloomDay: List[int], m: int, k: int) -> int:
        def solution_996_4_2(day):
            flowers=bouquet=0                
            for d in bloomDay:
                if d>day: flowers=0
                else:
                    flowers+=1
                    if flowers==k: bouquet+=1 ; flowers=0
            return bouquet>=m
            
        if len(bloomDay)<m*k: return -1       
        lo=min(bloomDay) ; hi=max(bloomDay)
        while lo<hi: 
            mid=(lo+hi)//2 
            if solution_996_4_2(mid): hi=mid          
            else: lo=mid+1
        return hi