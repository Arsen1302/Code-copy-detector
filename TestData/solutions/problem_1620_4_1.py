class Solution:
    def solution_1620_4_1(self, nums: List[int], numsDivide: List[int]) -> int:
            #define function to find gcd of array
        def solution_1620_4_2(a):
            #b is first element of array
            b = a[0]
            #loop thru rest of the array
            for j in range(1, len(a)):
                #if there's a new gcd, update b to it
                b=math.gcd(b,a[j])
            return b
        #find gcd of array numsDivide
        val = solution_1620_4_2(numsDivide)
        #use this to turn nums into a heap
        heapq.heapify(nums)
        #start count at zero
        count=0
        #loop while there are vals in nums
    #NB val%nums[0] - python sees 0 as false, so loop will stop when the % == 0
        while len(nums) > 0 and val%nums[0]:
            #increase count by 1
            count+=1
            #remove the smallest item from the heap
            heapq.heappop(nums)
        #if all items have been removed from nums
        if len(nums) > 0:
            #you know what this does
            return count
        #if there are still items in nums
        else:
            #as per question
            return -1