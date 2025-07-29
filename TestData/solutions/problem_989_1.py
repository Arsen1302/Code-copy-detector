class Solution:
    def solution_989_1(self, arr: List[int], k: int) -> List[int]:
        new_arr = []
        arr.sort()
        med = arr[int((len(arr) - 1)//2)]
        for num in arr : 
            new_arr.append([int(abs(num - med)), num])
            
        new_arr = sorted(new_arr, key = lambda x : (x[0], x[1]))
        
        output, counter = [], 0
        for i in reversed(range(len(new_arr))) : 
            output.append(new_arr[i][1])
            counter += 1 
            if counter == k : 
                return output 
            
        return output