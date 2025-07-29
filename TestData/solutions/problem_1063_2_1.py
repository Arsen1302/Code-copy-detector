class Solution:
    def solution_1063_2_1(self, arr: List[int]) -> int:
        st = 0
        end = len(arr) - 1
        prev = None
        
        st = Solution.solution_1063_2_2(arr=arr, st=0, inc_flag=True)
        end = Solution.solution_1063_2_2(arr=arr, st=len(arr)-1, inc_flag=False)

        merge_length = Solution.solution_1063_2_3(st-1, end+1, arr)
        take_first = len(arr) - st
        take_end = end + 1
        take_merged = len(arr) - merge_length
        return min(take_first, min(take_end, take_merged))
        
    @staticmethod
    def solution_1063_2_2(arr, st, inc_flag, prev=None):
        while(st < len(arr) if inc_flag else st >= 0):
            if prev is None or (arr[st] >= prev if inc_flag else arr[st] <= prev):
                prev = arr[st]
                st = st + 1 if inc_flag else st - 1
            else:
                break
        return st
    
    @staticmethod
    def solution_1063_2_3(first_arr_end, second_arr_st, arr):
        ans = 0
        first_arr_st = 0
        while(first_arr_st <= first_arr_end and second_arr_st < len(arr)):
            if arr[first_arr_st] <= arr[second_arr_st]:
                if first_arr_st >= second_arr_st:
                    ans = max(ans, len(arr) - 1)
                    break
                else:
                    ans = max(ans, first_arr_st + len(arr) - second_arr_st + 1)
                first_arr_st += 1
            else:
                second_arr_st += 1
        return ans