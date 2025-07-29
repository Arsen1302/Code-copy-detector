class Solution:
	def solution_724_5(self, stones: List[int]) -> int:
		stones.sort()
		while len(stones)>1:
			t = stones.pop()
			u = stones.pop()
			if t==u:
				continue
			else:
				stones.append(t-u)
				stones.sort()
		return stones[0] if stones else 0