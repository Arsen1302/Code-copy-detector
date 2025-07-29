class Solution:
    def solution_1538_3(self, nums: List[int], k: int) -> int:
        from sortedcontainers import SortedList
        if len(nums) == 1:
            return nums[0]+k
        
        arr = SortedList(nums)
        while k > 0:
            el = arr[0]
            arr.discard(el)
            arr.add(el+1)
            k -= 1
            
        product = 1
        for num in arr:
            product *= num
            product = product%(10**9+7)
        
        return product%(10**9+7)