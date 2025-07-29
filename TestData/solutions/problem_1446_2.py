class Solution:
    def solution_1446_2(self, prices: List[int]) -> int:
        result,count = 0,1
        for i in range(1,len(prices)):
            if prices[i] + 1 == prices[i-1]:
                count += 1
            else:
                result += (count * (count+1))//2
                count = 1
        result += (count * (count+1))//2
        return result