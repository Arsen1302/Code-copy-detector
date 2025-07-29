class Solution:
	def solution_169_4_1(self, words: List[str]) -> List[List[int]]:
		ht = {}
		for i in range(len(words)):
			ht[words[i]]=i
		res = []
		for i,word in enumerate(words):
			for j in range(len(word)+1):
				left,right=word[:j],word[j:]
				if self.solution_169_4_3(left) and right[::-1] in ht and i!=ht[right[::-1]]:
					res.append([ht[right[::-1]],i])
				if right and self.solution_169_4_3(right) and left[::-1] in ht and i!=ht[left[::-1]]:
					res.append([i,ht[left[::-1]]])
		return res

	def solution_169_4_2(self, words: List[str]) -> List[List[int]]:
		combs = [x for x in itertools.permutations([i for i in range(len(words))],2)]
		res = []
		for cm in combs:
			if self.solution_169_4_3(words[cm[0]]+words[cm[1]]):
				res.append(list(cm))
		# print(combs)
		return res

	def solution_169_4_3(self,s)->bool:
		return s==s[::-1]