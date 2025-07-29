class Solution:
	def solution_1482_2(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

		sc=0
		i=len(s)-1
		a=0
		m = (power**k)%modulo

		while i>-1:

			sc=(sc*power + ord(s[i])-97+1)%modulo

			if i+k<len(s):
				sc=(sc-((ord(s[i+k])-97+1)*m))%modulo

			if sc==hashValue:
				a=i
			i=i-1

		return s[a:a+k]