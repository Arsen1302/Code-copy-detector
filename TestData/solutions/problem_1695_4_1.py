class Solution:
    def solution_1695_4_1(self, nums: List[int]) -> int:
        def solution_1695_4_2(n):
            rem = 0
            while n!=0:
                digit = n%10
                n = n//10
                rem = rem*10+digit
            return rem
        
        rev_list = []
        for n in nums:
            rev_list.append(solution_1695_4_2(n))
            
        nums = set(nums+rev_list)
        return len(nums)