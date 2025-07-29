class Solution:
    def solution_1191_5(self, word1: str, word2: str) -> str:
        
        M = len(word1)
        N = len(word2)
        
        #pointers for word1 and word2
        p1 = 0
        p2 = 0
        
        mergeList = []
        while p1 < M and p2 < N:
            #print("mergeList: {}".format(mergeList))
            if word1[p1] > word2[p2]:
                mergeList.append(word1[p1])
                p1 += 1
            elif word1[p1] < word2[p2]:
                mergeList.append(word2[p2])
                p2 += 1
            else: #equal, so check ahead to see which one eventually has higher lex
                temp1,temp2 = p1,p2
                while word1[temp1] == word2[temp2]:
                    temp1 += 1
                    temp2 += 1
                    if temp2 == N:
                        #word2 reached the end without seeing different char from word1, so take word1's chars up till (and excluding) this point
                        #first make sure the next char in word1 is greater than word2's p2 char, otherwise we will take all of word2 first
                        if temp1 == M:
                            #both the same, take word1 char
                            mergeList.append(word1[p1])
                            p1 += 1
                            break
                        else:
                            if word1[temp1] < word2[p2]:
                                #take word2 char first
                                mergeList.append(word2[p2])
                                p2 += 1
                            else:
                                #take word1 first
                                mergeList.append(word1[p1])
                                p1 += 1
                        break
                    elif temp1 == M:
                        #similarly as the previous if
                        if temp2 == N:
                            #both the same - take word1 char first
                            mergeList.append(word1[p1])
                            p1 += 1
                        else:
                            if word2[temp2] < word1[p1]:
                                #take word1 char first
                                mergeList.append(word1[p1])
                                p1 += 1
                            else:
                                #take word2 char first
                                mergeList.append(word2[p2])
                                p2 += 1
                        break
                    elif word1[temp1] != word2[temp2]:
                        if word1[temp1] > word2[temp2]:
                            #char of word1 is bigger so take p1 char from word1
                            mergeList.append(word1[p1])
                            p1 += 1
                        else:
                            #char of word2 is bigger so take p2 char from word2
                            mergeList.append(word2[p2])
                            p2 += 1
                        break
        #done with at least one string, add the rest of the other
        if p1 == M and p2 != N:
            mergeList.append(word2[p2:])
        elif p1 != M and p2 == N:
            mergeList.append(word1[p1:])
        
        return "".join(mergeList)