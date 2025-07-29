class Solution:
    def solution_85_2(self, n: int) -> int:
        return int((('{0:032b}'.format(n))[::-1]),2)