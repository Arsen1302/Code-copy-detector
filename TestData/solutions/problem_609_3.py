class Solution(object):
    def solution_609_3(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        if N < 3:
            return [-1, -1]

        count_of_one = A.count(1)
        if count_of_one == 0:
            return [0, N-1]
        if count_of_one % 3 != 0:
            return [-1, -1]

        pattern = ''
        count = 0
        reversed_str = ''.join(map(str, A[::-1]))

        for i, digit in enumerate(A[::-1]):
            if digit == 1:
                count += 1
            if count == count_of_one/3:
                break
        pattern = reversed_str[:i+1]

        length = len(reversed_str)
        len_pattern = len(pattern)

        '''matching'''
        index = reversed_str.find(pattern, len_pattern)
        if index == -1:
            return [-1, -1]
        j = length - index

        index = reversed_str.find(pattern, len_pattern + index)
        if index == -1:
            return [-1, -1]
        i = length - index - 1

        return [i, j]