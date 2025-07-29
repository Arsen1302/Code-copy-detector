class Solution:
    def solution_537_1(self, seats: List[int]) -> int:
        #initialization, starting index is 0, result is res
        left,res,index = -1,0,0
        while index != len(seats):
            # only right is 1
            if left == -1 and seats[index] == 1:
                res = max(res,index)
                left = index
                index+=1
                continue
            # only left is 1
            if index == len(seats)-1 and seats[index] == 0:
                res = max(res,index-left)
                index+=1
                continue
            # left and right both 1, sitting in the middle
            if seats[index] == 1:
                res = max(res,(index-left)//2)
                left = index
            index+=1
        return res