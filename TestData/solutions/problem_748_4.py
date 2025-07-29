class Solution:
    def solution_748_4(self, candies: int, num_people: int) -> List[int]:
        distribution = 0
        iteration = 0
        past_distribution = 0
        
        while distribution <= candies:
            past_distribution = distribution
            iteration += 1
            distribution = ((num_people*iteration)*(num_people * iteration + 1))//2
            
        candies -= past_distribution
        ans = []
        for i in range(num_people):
            x = iteration-1
            ith_candies = (i+1)*(x) + (num_people*x*(x-1))//2
            
            if candies > 0:
                new_candy = (i+1) + ((iteration-1)*num_people)
                new_candies = min(candies, new_candy)
                ith_candies += new_candies
                candies -= new_candies
            ans.append(ith_candies)
        return ans