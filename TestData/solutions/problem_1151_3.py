class Solution:
    '''
    Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Maximum Binary String After Change.
	Memory Usage: 15.6 MB, less than 59.78% of Python3 online submissions for Maximum Binary String After Change.
    '''
	
	'''
	1. Variable Description -> first_zero => first occurence index of 0, num_zeros => Total number of zeros in the input binary string.
	2. If there are no zeros, directly return the binary string (Already in the desired form).
	3. Put all the ones(1) till first 0 occurence as it is and covert remaining num_zeros - 1 zeros to 1.
	3. Put the last remaining 0 now as we can't do anything about it.
	4. Now put the remaining 1s => (total length of binary string) - (count of zeros) - (count of ones at the beginning)
	'''
    def solution_1151_3(self, binary: str) -> str:
        first_zero, num_zeros = binary.find('0'), binary.count('0')
        return ('1' * ( first_zero + num_zeros - 1 )) + '0' + ('1' * (len(binary) - num_zeros - first_zero)) if zeros else binary