class Solution:
    def solution_1628_5(self, grades: List[int]) -> int:
        #we can solve by traversing linearly using one pointer!
        pointer = 0
        prev_sum, prev_size = 0,0 
        cur_sum, cur_size = 0,0 
        ans = 0
        #we have to make sure array is sorted in ascending order though!
        grades.sort()
        #as long as pointer is not out of bounds!
        while pointer < len(grades):
            #process current right element!
            cur_sum += grades[pointer]
            cur_size += 1
            #we formed a new group
            if(cur_sum > prev_sum and cur_size > prev_size):
                ans += 1
                prev_sum, prev_size = cur_sum, cur_size
                cur_sum, cur_size = 0, 0
                pointer += 1
                continue
            pointer += 1
        return ans