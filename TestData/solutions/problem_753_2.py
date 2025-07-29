class Solution:
    def solution_753_2(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [[0, 0] for i in range(n)]
        ans = []
        
        for i, j, k in bookings:
            arr[i-1][0] += k
            arr[j-1][1] += k
        
        curr = 0
        
        for i in range(len(arr)):
            ans.append(curr + arr[i][0])
            curr += arr[i][0] - arr[i][1]
    
        return ans