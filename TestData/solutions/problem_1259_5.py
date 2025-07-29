class Solution:
    def solution_1259_5(self, num: str, k: int) -> int:
        nums = [int(i) for i in num]
        orig = [int(i) for i in num]
        right = len(nums) - 1

        ans = 0
        for _ in range(k):
            for x in range(right, 0, -1):
                if nums[x] > nums[x-1]:
                    iter = x
                    mini = (float('inf'), -1)
                    while iter <= right:
                        # Number should be greater than nums[x-1]
                        # Number should be closer to nums[x-1] than the temp value at mini[0]
                        if nums[iter] > nums[x-1] and (mini[0] - nums[x-1]) > (nums[iter] - nums[x-1]):
                            mini = (nums[iter], iter)
                        iter += 1

                    # Swap the item found at index that is immediately greater than number at x-1
                    nums[x-1], nums[mini[1]] = nums[mini[1]], nums[x-1]
                    ans += (mini[1] - (x-1))

                    # Sort the numbers to the right of swapped number
                    nums[x:] = sorted(nums[x:])
                    # print ("".join([str(i) for i in nums]))
                    break

        # print (nums, orig)

        i = 0
        count = 0
        
        # minimum number of adjacent swaps to get to nums from orig. 
        # check where the number differs in the array and count the number of swaps to get the right number in the slot. 
        while i < len(nums):
            if nums[i] == orig[i]:
                i+=1
            else:
                j = i
                while nums[i] != orig[j]:
                    j+=1

                while j > i:
                    ## swap the number so that the calculations are correct as you traverse!
                    orig[j-1], orig[j] = orig[j], orig[j-1]
                    j -= 1
                    count += 1

        return count