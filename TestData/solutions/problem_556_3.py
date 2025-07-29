class Solution:
	def solution_556_3(self, n: int) -> bool:

		all_permutations = [] 

		for single_number in itertools.permutations(str(n)):

			if single_number[0] != '0':

				num = int(''.join(single_number))

				all_permutations.append(num)

		for i in range(32):

			if 2**i in all_permutations:
				return True

		return False