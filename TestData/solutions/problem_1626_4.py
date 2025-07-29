class Solution:
	def solution_1626_4(self, nums: List[int], k: int) -> int:
		# Count the Number of Bits in Each Unique Number - O(n)
		# Tally the Number of Times Each Bit Count Occurs - O(n)
		# Sort the (bit count, tally) pairs by bit count - O(nlogn)
		counts = sorted(Counter(map(int.bit_count, set(nums))).items()) # (I am fully aware that this line of code is really doing too much work)

		# Compute the Reversed Prefix Sum of the Tallies (i.e. sums[i] is how many numbers have at least counts[i][0] '1' bits) - O(n)
		sums = [0]*len(counts)
		sums[-1] = counts[-1][1]
		for i in range(len(sums) - 2, -1, -1):
			sums[i] += counts[i][1] + sums[i + 1]

		# Choose Each Number as the First Number of a Pair - O(nlogn)
		pairs = 0
		for n, c in counts:
			# Find the Smallest Number Which Forms a Valid Pair - O(logn)
			i = bisect_left(counts, k - n, key = lambda x: x[0])

			# Check if Any Pairs Can be Formed
			if i < len(sums):
				# Compute the Number of Pairs Which Start With the Given Collection of Numbers
				pairs += c*sums[i]

		# Return the Number of Pairs
		return pairs