class Solution:
    def solution_1326_4(self, heights: List[int]) -> List[int]:
        next_max = [-1 for i in range(len(heights))]
        res = [0 for i in range(len(heights))]
        for i in range(len(heights)-2, -1, -1):
            temp = i+1
            vis = 0
            while temp != -1:
                if heights[i] > heights[temp]:
                    vis += 1
                    temp = next_max[temp]
                else:
                    next_max[i] = temp
                    vis += 1
                    break
            res[i] = vis
        return res