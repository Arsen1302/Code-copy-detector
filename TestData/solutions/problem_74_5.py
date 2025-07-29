class Solution:
    def solution_74_5(self, numbers: List[int], target: int) -> List[int]:
        
        for left in range(len(numbers) -1): #1
            right = len(numbers) - 1 #2
            while left < right: #3
                temp_sum = numbers[left] + numbers[right] #4
                if temp_sum > target:  #5
                    right -= 1 #6
                elif temp_sum < target: #7
                    left +=1 #8
                else:
                    return [left+1, right+1] #9