class Solution:
    def solution_179_4_1(self, array, target):
        left = 0
        right = len(array) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def solution_179_4_2(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key = lambda x : [x[0], -x[1]])
        
        lis = []
        for width, height in envelopes:
            left = self.solution_179_4_1(lis, height)
            
            if left == len(lis):
                lis.append(height)
            else:
                lis[left] = height
                
        return len(lis)