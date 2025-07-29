class Solution:
    def solution_650_1(self, arr: List[int]) -> List[int]:

        if arr == sorted(arr):
            return []
        
        flips = []
        end = len(arr) - 1
        
        # find the max flip all the numbers from the first position to the max position 
        # ==> from 0 to max_position = k
        # ==> if max not at the end : flip again until the max is at the end of the array 
        # ==> from 0 to max_position = k
        # end = end - 1
        # repeat previous steps

        while end > 0:
            
            max_num = max(arr[:end+1])
            index_num = arr.index(max_num)
            
            if index_num != end:
                k = index_num + 1
                arr = arr[0:k][::-1] + arr[k:]
                flips.append(k)
                arr = arr[:end+1][::-1] + arr[end+1:]
                flips.append(end+1)
            else:
                k = end
                arr = arr[0:k][::-1] + arr[k:]
                flips.append(k)
            
            end -= 1

        return flips