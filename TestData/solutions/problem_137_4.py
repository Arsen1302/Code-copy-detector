class Solution:
    def solution_137_4(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 0, n
        if isBadVersion(1):
            return 1
        while L<R:
            mid = (L+R)//2
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1
        return L