class Solution:
    def solution_607_4(self, name: str, typed: str) -> bool:
        if len(set(name)) == len(set(typed)):
            i,j = 0,0
            while i < len(name):
                char = name[i]
                cnt_i = 1
                while i+1 < len(name) and name[i] == name[i+1]:
                    i += 1
                    cnt_i += 1
                if j < len(typed) and char == typed[j]:
                    cnt_j = 0
                    while j < len(typed):
                        if char == typed[j]:
                            j += 1
                            cnt_j += 1
                        else:
                            break
                else:
                    return False
                if cnt_i > cnt_j:
                    return False
                i += 1
            return True
        return False