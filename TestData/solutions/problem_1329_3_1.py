class Solution:
    def solution_1329_3_1(self, students, mentors):
        n, dict1 = len(students), defaultdict(int)

        for i in range(n):
            for j in range(n):
                dict1[i,j] = sum(k == l for k,l in zip(students[i],mentors[j]))

        @lru_cache(None)
        def solution_1329_3_2(i,mask):
            if i == n:
                return 0
            return max(solution_1329_3_2(i+1,mask-(1<<j)) + dict1[i,j] for j in range(n) if (1<<j)&amp;mask)

        return solution_1329_3_2(0,(1<<n)-1)