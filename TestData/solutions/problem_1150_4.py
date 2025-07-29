class Solution:
    def solution_1150_4(self, customers: List[List[int]]) -> float:
        s=0
        count=0
        flag=1
        for start, time in customers:
            if flag:
                count+=start
                flag=0
            if count>=start:
                count+=time
                s+=(count-start)
            else:
                s+=(time)
                count=start+time
            print(count, s)
        return s/len(customers)