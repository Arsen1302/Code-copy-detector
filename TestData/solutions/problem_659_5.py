class Solution:
    def solution_659_5(self, arr):
        n = len(arr)

        up, down = [0]*n, [0]*n

        up[0], down[0] = 1, 1

        for i in range(1,n):
            if arr[i] > arr[i-1]:
                up[i] = down[i-1] + 1
                down[i] = 1
            elif arr[i] < arr[i-1]:
                down[i] = up[i-1] + 1
                up[i] = 1
            else:
                up[i] = 1
                down[i] = 1

        return max(max(up),max(down))