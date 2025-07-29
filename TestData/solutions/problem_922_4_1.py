class Solution:
	def solution_922_4_1(self, n: int, reservedSeats: List[List[int]]) -> int:

		res = 0
		reserved = set()
		rowsTaken = {}

		# loop through reserved seats and add any reserved seats and add row to rowsTaken
		for r,c in reservedSeats:
			reserved.add((r, c))
			rowsTaken[r] = None

		# helper function to check if these 4 seats are available
		def solution_922_4_2(r, seats):
			nonlocal res
			for seat in seats:
				if seat in reserved:
					break
				if seat == seats[-1]:
					reserved.add(seat)
					res += 1

		# only loop through rows that have reserves seats, cause empty rows will always contain 2
		for row in rowsTaken.keys():
			solution_922_4_2(row, [(row,2), (row,3), (row,4), (row,5)])

			solution_922_4_2(row, [(row,4), (row,5), (row,6), (row,7)])

			solution_922_4_2(row, [(row,6), (row, 7), (row,8), (row,9)])

		# return our res + the (total rows - rowsTaken) which equals our empty rows, then multiply by two because 2 families can always fit in those rows
		return res + ((n - len(rowsTaken)) * 2)