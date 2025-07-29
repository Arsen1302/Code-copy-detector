class Solution:
    def solution_192_3(self, matrix: List[List[int]], k: int) -> int:
        temp_arr=[]
        for i in matrix:
            temp_arr.extend(i)
        temp_arr.sort()
        return temp_arr[k-1]