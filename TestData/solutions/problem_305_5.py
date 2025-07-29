`class Solution:
		def solution_305_5(self, word: str) -> bool:
			if word.isupper():
				return True
			elif word.islower():
				return True
			elif word.istitle():
				return True
			else:
				return False`