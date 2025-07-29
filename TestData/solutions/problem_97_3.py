class Solution:
    def solution_97_3(self, s: int, nums: List[int]) -> int:
        """
        O(N*LOG(N)) Solution using prefix-sum array 
        
        Since, we know all of the elements are positive, we can
        generate a prefix-sum array for the given nums array,
        which will be guaranteed to be in increasing order, aka a sorted list.
        
        Use this knowledge to then perform a binary search on the prefix-sum
        array for every element in the nums array, so that we can find the
        smallest sub-array starting from element at index = i with sum >= s, 
        IF there is one - there might be no sub-array from index = i to the end of
        the array that sums to s or more. For example, nums = [8, 2, 3] &amp; s = 8:
        There is no subarray starting from index 1 or 2 that sums to 8 or more, 
        only from index 0.
        """
        n = len(nums)
        if not n or sum(nums) < s:
            return 0
        # Generate prefix-sum array:
        #   [2,3,1,2,4,3] = nums
        # [0,2,5,6,8,12,15] = prefix-sum
        F = [num for num in nums]
        F.insert(0, 0)
        for i in range(1, n+1):
            F[i] += F[i-1]
        answer = float('inf') 
        # Perform binary search on the prefix-sums array
        # for every element in the nums array to get the
        # smallest sub-array starting from index i that sums
        # to s or more, IF there is one
        for i in range(n):
            l, r = i, n
            while l <= r:
                mid = (l+r)//2
                if F[mid] - F[i] >= s:
                    r = mid-1
                else:
                    l = mid + 1 
            if l <= n and F[l] - F[i] >= s:
                answer = min(answer, l-i)
        return answer if answer != float('inf') else 0