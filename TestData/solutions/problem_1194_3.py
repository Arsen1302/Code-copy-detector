class Solution:
    def solution_1194_3(self, s: str) -> int:
        i = j = 0
        n = len(s)
        res = 0
        
        while i < n:
            while j < n and s[j] == s[i]:
                j += 1
				
            # l is the length of  the homogenous substrings
            l = j - i
			# our formula goes here
            res += l * (l + 1) // 2
			# keep on iterating
            i = j
           
		# it is said in the problem to return answer modulo 10 ** 9 + 7
        return res % (10 ** 9 + 7)