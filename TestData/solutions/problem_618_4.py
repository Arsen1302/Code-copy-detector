class Solution:
    def solution_618_4(self, logs: List[str]) -> List[str]:
        if not logs:
            return 
        logs_l = []
        logs_d = []
        logs_sorted = []
        
        for log in logs:
            if log.split()[1].isdigit():
                logs_d.append(log)
            else:
                logs_l.append(log)
                m = log.split()[1:]
                m = ' '.join(m)
                print(m)
                logs_sorted.append(m)
        logs_sorted, logs_l = zip(*sorted(zip(logs_sorted, logs_l)))
        return list(logs_l) + logs_d