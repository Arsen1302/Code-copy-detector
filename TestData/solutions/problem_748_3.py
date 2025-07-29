class Solution:
    def solution_748_3(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        dist = 1
        pos = 0
        while candies > 0:
            if pos == num_people:
                pos = 0
            if candies < dist:
                res[pos] += candies
                return res
            res[pos] += dist
            candies -= dist
            dist += 1
            pos += 1
        return res