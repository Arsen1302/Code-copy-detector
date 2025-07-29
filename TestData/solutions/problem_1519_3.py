class Solution:
  def solution_1519_3(self, text: str, pattern: str) -> int:
    if pattern[0] == pattern[1]:
      letter = 1
      for i in range (len(text)) : 
        if text[i] == pattern[0] : letter += 1
      return letter*(letter-1)//2
    else :
      letter = 1
      ans1 = 0
      for i in range (len(text)) : 
        if   text[i] == pattern[0] : letter += 1
        elif text[i] == pattern[1] : ans1 += letter
          
      letter = 1
      ans2 = 0
      for i in range (len(text)-1, -1, -1) : 
        if   text[i] == pattern[1] : letter += 1
        elif text[i] == pattern[0] : ans2 += letter
      
      return max(ans1, ans2)