class Solution:
	def solution_512_4(self, sentence: str) -> str:
		lst = sentence.split(" ")

		lst2 = []

		vowels = ["a", "e", "i", "o", "u"]

		for i, word in enumerate(lst):
			tmp = word

			if (word[0].lower() in vowels):
				tmp = tmp + "ma"

			else: 
				tmp2 = tmp[1:] + tmp[0] + "ma" 
				tmp = tmp2

			tmp = tmp + ("a" * (i + 1))

			lst2.append(tmp)

		sentence_latin = " ".join(lst2)

		return sentence_latin