class Solution:
    def solution_1261_5(self, logs: List[List[int]]) -> int:
        # sort based on birth
        logs.sort()
        # an array to save info
        death_birth_years = []
        # maximum length
        maxlen = 0
        # output year 
        year = None
        # itearte over logs
        for i in logs:
            # if new birth is after min death year pop
            while(death_birth_years and i[0]  >= death_birth_years[0][0] ):
                heapq.heappop(death_birth_years)
            # push in inverted order ie, death, birth here
            heapq.heappush(death_birth_years, (i[1],i[0]))
            # check if it hits max length
            if len(death_birth_years) > maxlen:
                maxlen = max(len(death_birth_years),maxlen)
                # save the latest birth that trigged population peak
                year = i[0]
        # return the year
        return year