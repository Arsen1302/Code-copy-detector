class Solution:
  def solution_1569_5(self, words: List[str]) -> List[str]:
    key = ""
    result = []
    
    for word in words:
      letters = list(word)
      letters.sort()
      new_key = "".join(letters)
      
      if new_key != key :
        key = new_key
        result.append(word)
        
    return result