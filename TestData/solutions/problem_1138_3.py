class Solution:
    def solution_1138_3(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = length*[0]

        pos= sum([abs(item - nums[0]) for item in nums])   

        neg = 0
        output[0] = pos  

        for i in range(1,length):
            diff = nums[i] - nums[i-1]

            neg += diff*i
            pos -= diff*(length-i)

            output[i] = pos + neg
        
        return output




            
                    
            
            
        return summand_lst