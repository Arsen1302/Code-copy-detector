class Solution:
	def solution_831_5_1(self, products: List[str], searchWord: str) -> List[List[str]]:
		products.sort()
		obj = Trie()
		for product in products:
			obj.solution_831_5_3(product)

		final = []
		word = ''
		for char in searchWord:
			word += char
			final.append(obj.solution_831_5_4(word))

		return final
		
class Trie:
	def solution_831_5_2(self):
		self.root = dict()

	def solution_831_5_3(self, word):
		current = self.root
		for char in word:
			if char not in current:
				current[char] = dict()
			current = current[char]
		current['*'] = '*'

	def solution_831_5_4(self, word):
		current = self.root
		for char in word:
			if char not in current:
				return []
			current = current[char]
		self.result = []
		self.solution_831_5_5(current, word)
		if len(self.result) > 3:
			return self.result[:3]
		return self.result

	def solution_831_5_5(self, node, word):
		for value in node:
			if value == '*':
				self.result.append(word)
			else:
				self.solution_831_5_5(node[value], word+value)