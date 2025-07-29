class Solution:
    def solution_1305_2(self, nums: List[int]) -> int:
        
        nums.sort() # sorting the list, to access first 2 lowest elems &amp; 2 highest elems as we have to calulate max diff of pairs after product. 
        
        prod_pair_1 = nums[0] * nums[1] # product of 2 lowest elems in the list. 
        prod_pair_2 = nums[-1] *  nums[-2] # product of 2 highest elems in the list. 
        
        max_diff = prod_pair_2 - prod_pair_1 # calulating the diff of the product of the above mentioend two paris. 
        
        return max_diff # returning the max difference bet the product.