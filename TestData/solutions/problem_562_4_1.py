class Solution:
	def solution_562_4_1(self, piles: List[int], h: int) -> int:


		def solution_562_4_2(speed):

			return sum((pile-1) //speed+1 for pile in piles) <= h  # faster


			#hour=1
			#s=0
			#for pile in piles:
				#s+=pile
				#if s>speed:
					#s=pile
					#if hour>h:
						#return False
			#return True


		left, right = 1, max(piles)

		while left < right:
			mid = left  + (right - left) // 2
			if solution_562_4_2(mid):
				right = mid
			else:
				left = mid + 1
		return left