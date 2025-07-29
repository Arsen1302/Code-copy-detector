class Solution:
    def solution_1525_1_1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set_1 = solution_1525_1_2(nums1)
        set_2 = solution_1525_1_2(nums2)
        
        return solution_1525_1_3(set_1, set_2)
                
# Convert the lists into sets via helper method.      
def solution_1525_1_2(arr: List[int]):
    
    s = set()
    
    for i in arr:
        s.add(i)
        
    return s   

# Now when the two lists are sets, use the difference attribute to filter common elements of the two sets.
def solution_1525_1_3(x, y):
    
    x, y = list(x - y), list(y - x)
        
    return [x, y]


# Runtime: 185 ms, faster than 95.96% of Python3 online submissions for Find the Difference of Two Arrays.
# Memory Usage: 14.3 MB, less than 51.66% of Python3 online submissions for Find the Difference of Two Arrays.

# If you like my work, then I'll appreciate a like. Thanks!