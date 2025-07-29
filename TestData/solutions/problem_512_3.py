class Solution:
    def solution_512_3(self, S: str) -> str:
    	return " ".join([(s if s[0].lower() in 'aeiou' else s[1:]+s[0])+'maa'+'a'*i for i,s in enumerate(S.split())])


- Junaid Mansuri
(LeetCode ID)@hotmail.com