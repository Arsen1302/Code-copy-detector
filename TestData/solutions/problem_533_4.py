class Solution:
    def solution_533_4(self, arr):
        n = len(arr)

        left, right = [0]*n, [0]*n

        for i in range(1,n):
            if arr[i] > arr[i-1]:
                left[i] = left[i-1] + 1

        for j in range(n-2,-1,-1):
            if arr[j] > arr[j+1]:
                right[j] = right[j+1] + 1
                
        ans = [0]*n
        
        for i in range(n):
            if left[i] != 0 and right[i] != 0:
                ans[i] = left[i] + right[i] + 1
                
        return max(ans)