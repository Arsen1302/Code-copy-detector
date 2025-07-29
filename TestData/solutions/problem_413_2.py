class Solution:
    def solution_413_2(self, nums: List[int]) -> int:
        '''
        step 1: find the degree
            - create a hashmap of a number and value as list of occurance indices
            - the largest indices array in the hashmap gives us the degree
        step 2: find the minimum length subarray with same degree
            - initialize result as length of array
            - for each indices array, if it's length equals degree, means it's most frequent element
                - this length will be equal to the difference of first occurance and last occurance of most frequent element
                - compare this length with current result and keep the smallest length as result
            - return result + 1 because difference of indices will give us length - 1
                
            
        '''
        c = defaultdict(list)
        for i, n in enumerate(nums):
            c[n].append(i)        
        degree = max([len(x) for x in c.values()])
        
        result = len(nums)
        for indices in c.values():
            if len(indices) == degree:
                result = min(result, indices[-1] - indices[0])
        return result + 1