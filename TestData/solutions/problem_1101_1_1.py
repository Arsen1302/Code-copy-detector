class Solution:
    def solution_1101_1_1(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        def solution_1101_1_2(arr):
            
            arr.sort()

            dif = []
            
            for i in range(len(arr) - 1):
                dif.append(arr[i] - arr[i + 1])
            
            return len(set(dif)) == 1
        
        for i , j in zip(l , r):
            ans.append(solution_1101_1_2(nums[i:j + 1]))
        
        return ans