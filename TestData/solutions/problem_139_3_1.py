class Solution:
    def solution_139_3_1(self, num: str, target: int) -> List[str]:
        answer = set()
        
        def solution_139_3_2(idx, total, path, last_number):
            if idx == len(num) and total == target:
                answer.add(path)
                
            if idx >= len(num):
                return
            
            for i in range(idx, len(num)):
                if len(num[idx:i+1]) > 1 and num[idx:i+1][0] == "0":
                    continue
                    
                tmp_number = num[idx:i+1]
                
                if last_number == "":
                    solution_139_3_2(i + 1, int(tmp_number), tmp_number, tmp_number)
                else:
                    # addition
                    solution_139_3_2(i + 1,total + int(tmp_number), path + "+" + tmp_number, tmp_number)
                    
                    # subtraction
                    solution_139_3_2(i + 1,total - int(tmp_number), path + "-" + tmp_number, "-" + tmp_number)
                    
                    # multiplication
                    solution_139_3_2(i + 1, total-int(last_number) + (int(last_number) * int(tmp_number)), path + "*" + tmp_number, str(int(tmp_number) * int(last_number)))

        solution_139_3_2(0,-1,"", "")
        return answer