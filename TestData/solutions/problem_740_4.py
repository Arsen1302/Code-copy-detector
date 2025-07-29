class Solution(object):
    def solution_740_4(self, arr):
        x = 0
        while x < len(arr):
            if arr[x] == 0:
                arr.insert(x, 0)
                arr.pop(-1)
                x+=1
            x += 1