class Solution:
    def solution_748_5(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        n = 1
        while candies:
            for i in range(num_people):
                res[i] += n
                candies -= n
                if candies < 0:
                    res[i] -= n
                    res[i] += n + candies
                    return res
            
                n += 1
                
        return res