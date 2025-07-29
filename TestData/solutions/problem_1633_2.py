class Solution:
    def solution_1633_2(self, tasks: List[int], space: int) -> int:
        Dict = {}
        ans,l = 0,len(tasks)
        
        for i,n in enumerate(tasks):
            if n in Dict:
                ans += max(1,space-(ans-Dict[n])+1)
            else:
                ans+=1
            Dict[n] = ans
        return ans