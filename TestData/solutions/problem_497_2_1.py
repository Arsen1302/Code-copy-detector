class Solution:
   def solution_497_2_1(self, s: str, words) -> int:

       def solution_497_2_2 (s):
           wordTable = []
           repeatCounter = 1
           solution_497_2_2 = ""
           for i in range(len(s)):
               if i == 0:
                   continue
               if s[i] == s[i-1]:
                   repeatCounter += 1
               else:
                   solution_497_2_2 += s[i-1]
                   wordTable.append(repeatCounter)
                   repeatCounter = 1
                   
           else:
               solution_497_2_2 += s[len(s)-1]
               wordTable.append(repeatCounter)
               
           return solution_497_2_2, wordTable
   
       
       matchCounter = 0
       sampleCondenseWord, sampleWordTable = solution_497_2_2(s)
       for word in words:
           testCondenseWord, testWordTable = solution_497_2_2(word)
           if sampleCondenseWord == testCondenseWord:
               for i in range(len(sampleCondenseWord)):
                   if sampleWordTable[i] >= 3 and sampleWordTable[i] < testWordTable[i]:
                       break
                   if sampleWordTable[i] < 3 and sampleWordTable[i] != testWordTable[i]:
                       break
               else:
                   matchCounter += 1
       
       return matchCounter