class Solution:
    def solution_875_5(self, n: int, ranges: List[int]) -> int:
        # Convert to right sided sprinklers
        # Instead of picturing sprinklers at the center of their range
        # picture them at the left most possible position in their range
        for i in range(len(ranges)):
            r = ranges[i]
            # Remove the sprinkler from its current position
            ranges[i] = 0
            left_placement = max(0, i - r)
            right_range = i + r - left_placement
            # If multiple sprinklers are compteing for same spot
            # we ignore all except the sprinkler with the max range
            ranges[left_placement] = max(ranges[left_placement], right_range)
        
        # Ranges has now been converted to the same format as Jump Game II
        # Similar to https://leetcode.com/problems/jump-game-ii/
        max_reach = jump_limit = jumps = 0
        for pos in range(len(ranges)):
            if pos > max_reach:
                return -1
            if pos > jump_limit:
                jump_limit = max_reach
                jumps += 1
            max_reach = max(max_reach, pos + ranges[pos])
        return jumps