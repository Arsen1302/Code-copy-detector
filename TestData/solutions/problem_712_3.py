class Solution:
    def solution_712_3(self, a: int, b: int, c: int) -> List[int]:

        # sort the three integers
        sorti = sorted([a, b, c])

        # get the minimum number
        diff = [sorti[1] - sorti[0], sorti[2] - sorti[1]]

        # go through the cases for the minimum
        if diff[0] == 1 and diff[1] == 1:
            minimum = 0
        elif (diff[0] == 2 or diff[1] == 2) or (diff[0] == 1 or diff[1] == 1):
            minimum = 1
        else:
            minimum = 2
        
        # get the maximum number of differences between min and max
        # which would be sorti[2] - sorti[0]
        # and subtract the stone in between (as there is one occupied place)
        maximum = sorti[2] - sorti[0] - 2
        return minimum, maximum