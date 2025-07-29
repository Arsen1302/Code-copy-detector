class Solution:
    def solution_1606_5(self, key: str, message: str) -> str:
        res = {}
        char = 97 
        for i in key:
            if i not in res and i!=" ":
                res[i] = chr(char)
                char+=1
            if i == " ":
                res[i] = " "
        decoded = ""
        for i in message:
            if i!=" ":
              decoded+=res[i]
            else:
                decoded+=" "
        return decoded