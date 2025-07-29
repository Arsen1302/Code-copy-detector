class Solution:
    def solution_1072_5(self, arr: List[int]) -> int:
        # We check how many times each element in arr occurs in odd length subarray and finally multiply the value with its freq and add it to our ans
        # TC: O(n) and SC: O(n)
        # Total no. of subarrays including arr[i] is = No. of subarrays ending at arr[i] * no. of subarrays beginning with arr[i]
        # No. of odd length subarrays would be half of total subarrays, but since when total no. of subarrays could be odd, so we add 1 to total and then divide by 2 to get odd length subarrays containing the value
        
        ans = 0
        for i in range(len(arr)):
            ne = i+1
            ns = len(arr)-i
            total = ne*ns
            nodd = (total+1)//2
            ans+=(arr[i]*nodd)
        return ans