class Solution:
    def solution_301_1_1(self, s: str) -> int:
        return self.solution_301_1_2(0, len(s)-1, s)
    
    def solution_301_1_2(self, start, end, s):
        """
            method used to find the longest palindrome subsequence in a string
            start: start index of the string
            end: end index of the string
            s: string
            return: length of the longest palindrome subsequence
        """
        if start == end:
            return 1
			
        if start > end:
            return 0

        if s[start] == s[end]:
            return 2 + self.solution_301_1_2(start + 1, end - 1, s)
        
        return max(self.solution_301_1_2(start + 1, end, s), self.solution_301_1_2(start, end - 1, s))