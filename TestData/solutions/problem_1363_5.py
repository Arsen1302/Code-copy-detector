class Solution:
			def solution_1363_5(self, nums: List[int]) -> int:
				quadruplet_count = 0
				
				for a, b, c, d in itertools.combinations(nums, 4):
					if (a + b + c) == d:
						quadruplet_count += 1

				return quadruplet_count