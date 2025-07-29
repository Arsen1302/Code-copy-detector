class Solution:
	def solution_301_3(self, s: str) -> int:
        # use dp approach
        # create a 2d array to store the result
        L = [ [0 for _ in range(len(s))] for _ in range(len(s)) ]
        # initialize the first row and column: strings of length 1 are palindromes of length 1
        for i in range(len(s)):
            L[i][i] = 1
        
        for len_subseq in range(2, len(s) + 1):
            for start in range(len(s) - len_subseq + 1):
                end = start + len_subseq - 1
                # if the string is palindrome, the length is 2
                if s[start] == s[end]:
                    L[start][end] = 2 + L[start+1][end-1]
                # if the string is not palindrome, the length is the max of the length of the string
                # with the same start index and the length of the string with the same end index
                else:
                    L[start][end] = max(L[start+1][end], L[start][end-1])
        # return the length of the longest palindrome subsequence
        return L[0][len(s)-1]