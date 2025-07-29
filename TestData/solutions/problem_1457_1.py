class Solution:
    def solution_1457_1(self, bank: List[str]) -> int:
        a, s = [x.count("1") for x in bank if x.count("1")], 0

		# ex: bank is [[00101], [01001], [00000], [11011]]
		# a would return [2, 2, 4]

        for c in range(len(a)-1):
            s += (a[c]*a[c+1])

			# basic math to find the total amount of lasers
			# for the first iteration: s += 2*2
			# for the second iteration: s += 2*4
			# returns s = 12

        return s