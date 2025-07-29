class Solution:
    def solution_1214_3(self, nums: List[int], limit: int, goal: int) -> int:
        """
        1) Take the sum of nums
        2) Chech how many steps it is aways from goal
        3) Divide the steps w.r.t limit
        4) The ceiling of the division will give you
           no. of hopes required to reach that goal
        """
        return math.ceil(abs(goal - sum(nums))/limit)