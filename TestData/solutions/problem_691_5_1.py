class Solution:
	def solution_691_5_1(self, weights: List[int], days: int) -> int:


		def solution_691_5_2(capacity):
			day=1
			total=0

			for weight in weights:
				total+=weight

				if total>capacity:  #if there is no space in ship belt,go to next days
					total=weight
					day+=1

					if day>days:  #if total day exceeds the days
						return False
			return True



		left,right=max(weights),sum(weights)  #capacity should be at least max(weights) and capacity need not be more than sum(weights)

		while left<right:

			mid=left+(right-left)//2

			if solution_691_5_2(mid):
				right=mid
			else:
				left=mid+1
		return left