class Solution:
    def solution_1415_5(self, word1: str, word2: str) -> bool: 
        d1={}
        d2={} 

        #FREQUENCIES OF WORD1 CHARACTERS
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1 

        #FREQUENCIES OF WORD2 CHARACTERS
        for i in word2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1 

        #CHECK IF EQUAL CHARACTERS OF WORD1 AND WORD2 HAVING FREQUENCY DIFFERENCE AT MOST 3
        #AND IF CHARACTERS PRESENT IN d1 BUT NOT d2 ,CHECK FRQUENCY OF d1 CHARACTERS SHOULD BE AT MOST 3 
        #AS FREQUENCY - 0(COZ NOT PRESENT IN D2) 
        for i in d1.keys():
            if i in d2:
                if not(abs(d2[i]-d1[i])<=3):
                    return False 
            else:
                if not(d1[i]<=3):
                    return False

        #IF CHARACTERS PRESENT IN d2 BUT NOT d1 ,CHECK FRQUENCY OF d2 CHARACTERS SHOULD BE AT MOST 3 
        #AS FREQUENCY - 0(COZ NOT PRESENT IN D1) 
        for i in d2.keys():
            if i not in d1:
                if not(d2[i]<=3):
                    return False 
        #REMOVED ALL FALSE CONDITIONS ABOVE, RETURN TRUE
        return True