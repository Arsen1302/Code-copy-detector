class Solution:
    def solution_492_2(self, words: List[str]) -> int:
    	M = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    	return len(set([''.join(map(lambda x: M[ord(x)-97], w)) for w in words]))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com