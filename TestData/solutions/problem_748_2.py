class Solution:
    def solution_748_2(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        index = 0
        while candies > 0:
            res[index % num_people] += min(index + 1, candies)
            index += 1
            candies -= index
        return res