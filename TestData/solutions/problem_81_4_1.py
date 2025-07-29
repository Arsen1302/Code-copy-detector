class Solution:
    def solution_81_4_1(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums = self.solution_81_4_3(nums)
        return str(int("".join(nums)))
    
    def solution_81_4_2(self, n1, n2):
        return n1 + n2 > n2 + n1
    
    def solution_81_4_3(self, nums):
        length = len(nums)
        if length > 1:
            middle = length //2
            left_list = self.solution_81_4_3(nums[:middle])
            right_list = self.solution_81_4_3(nums[middle:])
            nums = self.solution_81_4_4(left_list,right_list)
        return nums

    def solution_81_4_4(self,list1,list2):
        result = []
        l1 = deque(list1)
        l2 = deque(list2)
        while l1 and l2:
            if self.solution_81_4_2(l1[0],l2[0]):
                result.append(l1[0])
                l1.popleft()
            else:
                result.append(l2[0])
                l2.popleft()
        result.extend(l1 or l2)
        return result