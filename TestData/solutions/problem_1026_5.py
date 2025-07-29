class Solution:
	def solution_1026_5(self, arr: List[int]) -> int:
		if arr[0] % 2 == 0:
			dpOdd = [0] * len(arr)
			dpEven = [1]  + [0] * (len(arr)-1)
			result = 0

		else:
			dpOdd = [1]  + [0] * (len(arr)-1)
			dpEven = [0] * len(arr)
			result = 1

		for i in range(1,len(arr)):
			if arr[i] % 2 == 1:
				dpOdd[i] += 1 + dpEven[i-1]
				dpEven[i] += dpOdd[i-1]

			else:
				dpOdd[i] += dpOdd[i-1]
				dpEven[i] += 1 + dpEven[i-1]

			result += dpOdd[i]


		return result % (10**9 + 7)