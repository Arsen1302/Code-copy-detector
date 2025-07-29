class Solution:
    def solution_1534_3(self, matches: List[List[int]]) -> List[List[int]]:
        win = []
        loss = []
        hashmap = {}
        occur = set()
        for values in matches:
           
            wins = values[0]
            losss = values[1]
            

            if wins not in hashmap:
                hashmap[wins] = 1
            if losss not in hashmap:
                hashmap[losss] = 0

            
            if wins in hashmap and hashmap[wins] == 0 and hashmap[wins] != -1 and wins in occur:
                hashmap[wins] = 0
            if losss in hashmap and hashmap[losss] == 0 and losss in occur:
                hashmap[losss] = -1
            if losss in hashmap and hashmap[losss] == 1 and hashmap[losss] != -1 and losss in occur:
                hashmap[losss] = 0
            if wins in hashmap and hashmap[wins] == 1 and hashmap[wins] != -1 and wins in occur:
                hashmap[wins] = 1

            occur.add(wins)
            occur.add(losss)

        for i in hashmap:
            if hashmap[i] == 0:
                loss.append(i)
            if hashmap[i] == 1:
                win.append(i)
        
        win.sort()
        loss.sort()

        return [win, loss]