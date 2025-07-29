class Solution(object):
    def solution_1332_5(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        milestones.sort()
        s = sum(milestones[:-1])
        if milestones[-1] > s:
            return s * 2 + 1
        else:
            return s + milestones[-1]