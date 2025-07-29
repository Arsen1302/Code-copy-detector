class Solution:
    def solution_1072_4(self, arr: List[int]) -> int:
        
        length = len(arr)
        ans = 0
        
        for i in range(length) :
            ans += ((i+1)*(length-i)+1)//2 * arr[i]
        return ans;