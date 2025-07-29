class Solution:
	def solution_534_3(self, hand: List[int], groupSize: int) -> bool:
		if len(hand)%groupSize!=0:
			return False

		dic = Counter(hand)
		keys = sorted(dic.keys())
		for k in keys:
			f = dic[k]
			if f!=0:
				for j in range(1,groupSize):
					if dic[k+j]<f:
						return False
					dic[k+j]-=f

		return True