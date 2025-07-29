class Solution(object):
    def solution_1606_3(self, key, message):
        mapping={' ':' '}
        alphabet='abcdefghijklmnopqrstuvwxyz'
        res=''
        i=0
        for eachchar in key:
            if eachchar not in mapping:
                mapping[eachchar]=alphabet[i]
                i+=1
        print(mapping)
        for j in message:
            res+=mapping[j]
        return res