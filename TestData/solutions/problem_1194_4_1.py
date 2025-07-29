class Solution:
    def solution_1194_4_1(self, s: str) -> int:
		# Function to calculate total possible substring
		# from a contiguous subarray having the same character
        def solution_1194_4_2(n):
            return (n * (n + 1)) // 2
		i = sumn = 0
		n = 1               # The starting value for any character
        while i < len(s) - 1:
			# Keep incrementing n until different characters are encountered
            if s[i] == s[i + 1]:
                n += 1
            else:
				# Add all the cases for that substring and initialize n = 1
                sumn += solution_1194_4_2(n)
                n = 1
            i += 1
		# For the last index of the array (Since, the loop will only run till n - 1)
        sumn += solution_1194_4_2(n)
        return sumn % (pow(10, 9) + 7)