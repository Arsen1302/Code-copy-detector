class Solution:
    def solution_1151_4(self, binary: str) -> str:
        # Find the first zero
        first_zero = binary.find('0')
		# If there are no zeroes then no optimization is needed
        if(first_zero == -1):
            return binary
		# Counting number of zeros
        count_zeroes = binary.count('0', first_zero)

        return '1' * (first_zero) + '1' * (count_zeroes-1) + '0' + '1' * (len(binary) - first_zero - count_zeroes)