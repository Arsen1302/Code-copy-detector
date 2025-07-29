class Solution:
    def solution_1328_5(self, num: str, change: List[int]) -> str:
        
        # Converted nums to list
        nums = list(num)
        updated = False
        
        for i in range(len(nums)):
            # Get value at ith index
            val = int(nums[i])
            # If we can change it to greater value then swap and updated is True
            if(val < change[val]):
                nums[i] = str(change[val])
                updated = True
            # If we have already updated to a greater value but that is now not valid then break
            # Since, We can mutate only one substring
            elif(val > change[val] and updated is True):
                break
        return ''.join(nums)