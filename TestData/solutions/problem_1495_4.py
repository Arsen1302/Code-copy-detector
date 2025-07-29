class Solution(object):
    def solution_1495_4(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3==0:
            l=num//3
            return [l-1,l,l+1]
        return []