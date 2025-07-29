class Solution:
    def solution_464_1(self, J: str, S: str) -> int:
    	return sum(i in J for i in S)



class Solution:
    def solution_464_1(self, J: str, S: str) -> int:
    	return sum(S.count(i) for i in J)



from collections import Counter

class Solution:
    def solution_464_1(self, J: str, S: str) -> int:
    	return sum(Counter(S)[i] for i in J)
		
		

- Junaid Mansuri
(LeetCode ID)@hotmail.com