class Solution:
    def solution_884_3(self, G: List[List[int]], k: int) -> List[int]:
        return [r[1] for r in heapq.nsmallest(k,[[sum(g),i] for i,g in enumerate(G)])]
		
		
- Junaid Mansuri
- Chicago, IL