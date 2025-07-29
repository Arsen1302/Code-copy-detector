class Solution:
    def solution_797_1(self, A: List[int]) -> bool:
    	return (lambda x: len(x) == len(set(x)))(collections.Counter(A).values())
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com