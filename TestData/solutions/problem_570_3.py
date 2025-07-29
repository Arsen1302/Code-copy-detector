class Solution:
    def solution_570_3(self, G: List[List[int]]) -> int:
    	return sum([1 for i in G for j in i if j != 0]+[max(i) for i in G]+[max(i) for i in list(zip(*G))])
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com