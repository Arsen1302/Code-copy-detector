class Solution:
    def solution_381_4_1(self, nums: List[int]) -> Optional[TreeNode]:
            
            
        def solution_381_4_2(num: list):
            
            if len(num):
                max_number  = max(num)
                max_index   = num.index(max_number)

                left = num[0:max_index]
                right = num[max_index+1:]

                return TreeNode(val=max_number, left=solution_381_4_2(left), right=solution_381_4_2(right))
            
        return  solution_381_4_2(nums)