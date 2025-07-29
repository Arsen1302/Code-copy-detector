class Solution:
    def solution_603_3(self, S: str) -> int:
        S, t = ' ' + S + ' ', 0
        while 1:
            while '()' in S: S = S.replace('()','')
            if len(S) <= 3: return t + len(S) - 2
            while S[1] == ')': t, S = t + 1, ' ' + S[2:]
            while S[-2] == '(': t, S = t + 1, S[:-2] + ' '
			
			
- Junaid Mansuri
- Chicago, IL