class Solution(object):
    def solution_1385_4(self, s):
        """
        :type s: str
        :rtype: int
        """
		 ans, l = 0, 0
        while l < len(s):
            if s[l] == 'X':
                l+=3
                ans +=1
            else:
                l+=1
        return ans