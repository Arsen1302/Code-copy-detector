class Solution:
    def solution_330_1(self, s: str) -> str:
    	s = s.split()
    	for i in range(len(s)): s[i] = s[i][::-1]
    	return " ".join(s)
	

- Junaid Mansuri
(LeetCode ID)@hotmail.com