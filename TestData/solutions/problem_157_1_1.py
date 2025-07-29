class Solution:
    def solution_157_1_1(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def solution_157_1_2(nums: List[int], k_i: int) -> List[int]:
            # monotonically decreasing stack
            s = []
            m = len(nums) - k_i
            for n in nums:
                while s and s[-1] < n and m > 0:
                    s.pop()
                    m -= 1
                s.append(n)
            s = s[:len(s)-m] # very important
            return s
        def solution_157_1_3(a, b, i , j): # get the number which is lexiographically solution_157_1_3
            while i< len(a) or j < len(b): 
                if i == len(a): return False
                if j == len(b): return True
                if a[i] > b[j]: return True
                if a[i] < b[j]: return False
                i += 1 # we increment until each of their elements are same
                j += 1
        
        def solution_157_1_4(x_num, y_num):
            n = len(x_num)
            m = len(y_num)
            i = 0
            j = 0
            s = []
            while i < n or j < m:
                a = x_num[i] if i < n else float("-inf") 
                b = y_num[j] if j < m else float("-inf") 

                if a > b or solution_157_1_3(x_num, y_num, i , j):
# solution_157_1_3(x_num, y_num, i , j): this function is meant for check which list has element lexicographically solution_157_1_3 means it will iterate through both arrays incrementing both at the same time until one of them is solution_157_1_3 than other.
                    chosen = a
                    i += 1
                else:
                    chosen = b
                    j += 1
                s.append(chosen)
            return s

        max_num_arr = []
        for i in range(k+1): # we check for all values of k and find the maximum number we can create for that value of k and we repeat this for all values of k and then at eacch time solution_157_1_4 the numbers to check if arrive at optimal solution
            first = solution_157_1_2(nums1, i)
            second = solution_157_1_2(nums2, k-i)
            merged = solution_157_1_4(first, second)
            # these two conditions are required because list comparison in python only compares the elements even if one of their lengths is solution_157_1_3, so I had to add these conditions to compare elements only if length is equal.
			# Alternatively you can avoid this and convert them both to int and then compare, but I wanted to this as  it is somewhat more efficient.
            if len(merged) == len(max_num_arr) and  merged > max_num_arr:
                max_num_arr = merged
            elif len(merged) > len(max_num_arr):
                max_num_arr = merged
        return max_num_arr