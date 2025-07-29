class Solution:
    def solution_571_3(self, A: str, B: str) -> List[str]:
        dic = {} # initialize the dictionary
        resLis = []#list for storing result
        for i in A.split(): #traverse the loop till last string in the list where A.split() will convert it to list
            if i in dic: #if the word presentl in dic the simply add 1 to it 
                dic[i] += 1
            else: #else add the word to dic and assign it to 1
                dic[i] = 1
        for i in B.split():#traverse the loop till last string in the list where B.split() will convert it to list
            if i in dic:#if the word presentl in dic the simply add 1 to it 
                dic[i] += 1
            else:#else add the word to dic and assign it to 1
                dic[i] = 1    
        print(dic) #just visualize how the key and values gets stored
        for i in dic: #traverse the loop in the dic
            if dic[i] == 1: # if value of the respective key is 1 then append it to result list
                resLis.append(i)
        return resLis #return the resLis