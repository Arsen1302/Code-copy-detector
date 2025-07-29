class Solution:
    def solution_935_5_1(self, satisfaction: List[int]) -> int:
		n = len(satisfaction)
		satisfaction.sort()

		@cache
		def solution_935_5_2(dish, time):
			if dish == n:
				return 0

			cook = satisfaction[dish] * (time + 1) + solution_935_5_2(dish + 1, time + 1)
			skip = solution_935_5_2(dish + 1, time)

			return max(cook, skip)

		return solution_935_5_2(0, 0)