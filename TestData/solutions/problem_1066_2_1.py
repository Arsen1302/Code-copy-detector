class Solution:
    
    def solution_1066_2_1(self, nums1: List[int], nums2: List[int]) -> int:
        """
        O(n^2)
        """
        
        def solution_1066_2_2(nums1, nums2):
            
            # Initialize a dict: value->(value^2, count)
            a = {}
            for i in nums1:
                if i not in a:
                    a[i] = [i**2, 1]
                else:
                    a[i][-1] += 1
                               
            # Initialize a dict: nums2[i] * nums[j] -> count
            b = collections.defaultdict(int)
            for i in range(len(nums2)):
                for j in range(i+1, len(nums2)):
                    b[nums2[i]*nums2[j]] += 1
                    
            # Calculate the result
            # result += i^2 count * j*k count for each combination
            result = 0            
            for (i, amount) in a.values():                
                result += b[i]*amount
            
            return result
        
                                
        # Call above function twice
        return solution_1066_2_2(nums1, nums2) + solution_1066_2_2(nums2, nums1)