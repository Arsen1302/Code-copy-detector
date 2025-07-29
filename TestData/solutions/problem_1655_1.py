class Solution:
    def solution_1655_1(self, nums: List[int]) -> bool:
    """ 
	Bruteforce approch
	"""
#         for i in range(len(nums)-2):
#             summ1 = nums[i] + nums[i+1]
#             # for j in range(i+1,len(nums)):
#             for j in range(i+1,len(nums)-1):
#                 summ = nums[j] + nums[j+1]
#                 if summ == summ1:
#                     return True
#         return False
	 """
	 Sliding Window
	 """
        one ,two = len(nums)-2,len(nums)-1      // at end of list
        dic = {}
        while one >= 0:
            # print(one,two)
            summ = nums[one] + nums[two]
            if summ in dic:
                return True               // if already there then there is 2 pairs
            else:
                dic[summ] = 1        // add summ in of window in dictonary
            one -=1
            two -=1
        return False