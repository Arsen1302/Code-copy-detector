class Solution:
    def solution_1181_4(self, lowLimit: int, highLimit: int) -> int:
        res = 0
        boxes = collections.defaultdict(int)
        for num in range(lowLimit, highLimit+1):
            box = 0
            while num:
                digit = num%10
                num = num//10
                box += digit
            boxes[box] +=1
            res = max(res, boxes[box])
        return res