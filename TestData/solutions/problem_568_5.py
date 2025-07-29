class Solution:
    def solution_568_5(self, people: List[int], limit: int) -> int:

        res = 0
        people.sort()

        left = 0
        right = len(people) - 1

        while left <= right:

            weight = people[left] + people[right]
            
            if weight <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            res += 1
        
        return res