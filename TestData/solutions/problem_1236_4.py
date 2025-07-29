class Solution:
    def solution_1236_4(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        users = {}
        for id,time in logs:
            if id not in users:
                users[id] = set()
                users[id].add(time)
            else:
                users[id].add(time)


        for user in users:
            res[len(users[user])-1]+=1
        return res