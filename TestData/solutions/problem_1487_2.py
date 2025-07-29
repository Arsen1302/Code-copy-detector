class Solution:
    def solution_1487_2(self, nums: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for i in range(len(nums)):
            if((i%2)==0):
                even_list.append(nums[i])
            else:
                odd_list.append(nums[i])
        even_list = sorted(even_list)
        odd_list = sorted(odd_list, reverse = True)
        i=0; j=0
        for m in range(len(nums)):
            if m&amp;1:
                nums[m] = odd_list[j]
                j+=1
            else:
                nums[m] = even_list[i]
                i+=1
        return nums