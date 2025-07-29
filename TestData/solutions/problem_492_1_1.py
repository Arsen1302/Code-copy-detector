class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	MORSE = {
		'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
		'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
		'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
		'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
	}

	def solution_492_1_1(self, words: List[str]) -> int:
		return len(set(map(self.solution_492_1_2, words)))

	@classmethod
	def solution_492_1_2(cls, word: str) -> str:
		return ''.join(map(cls.MORSE.get, word))