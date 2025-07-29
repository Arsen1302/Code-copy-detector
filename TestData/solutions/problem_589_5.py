class Solution:
    def solution_589_5(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        for ele in nums:
            if ele%2==0:
                list1.append(ele)
            else:
                list2.append(ele)
        return list1+list2