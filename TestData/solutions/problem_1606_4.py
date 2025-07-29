class Solution:
    def solution_1606_4(self, key: str, message: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        y = key.replace(" ","")
        al = [i for i in alpha]
        ke = []
        for i in y :
            if i not in ke:
                ke.append(i)
        nano = [i for i in zip(ke,al)]
        nano.append([" ", " "])
        nano1 = []
        nano2 = []
        for i in nano:
            nano1.append(i[0])
        for i in nano:
            nano2.append(i[1])
        dec = ""
        for i in message:
            ind = nano1.index(i)
            dec += nano2[ind]
        return dec