class Solution:
    def solution_301_2_1(self, s: str) -> int:
        # add 2d list memo to avoid redundant calculation
        self.memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        return self.solution_301_2_2(0, len(s)-1, s)
    
    def solution_301_2_2(self, start, end, s):
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

        # if the value is in the memo, return the value
        if self.memo[start][end] != 0:
            return self.memo[start][end]

        # if the value is not in the memo, calculate the value
        # then add the value to the memo
        if s[start] == s[end]:
            self.memo[start][end] = 2 + self.solution_301_2_2(start + 1, end - 1, s)
        else:
            self.memo[start][end] = max(self.solution_301_2_2(start + 1, end, s), self.solution_301_2_2(start, end - 1, s))
            
        return self.memo[start][end]