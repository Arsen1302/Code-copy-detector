class Solution:
	def solution_101_3_1(self, s: str) -> str:
		def solution_101_3_2(txt, patt):
			newString = patt + '#' + txt
			freqArray = [0 for _ in range(len(newString))]
			i = 1
			length = 0
			while i < len(newString):
				if newString[i] == newString[length]:
					length += 1
					freqArray[i] = length
					i += 1
				else:
					if length > 0:
						length = freqArray[length - 1]
					else:
						freqArray[i] = 0
						i += 1
			return freqArray[-1]
		cnt = solution_101_3_2(s[::-1],s)
		return s[cnt:][::-1]+s