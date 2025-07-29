class Solution:
  def solution_1558_4(self, cards: List[int]) -> int:
    table = dict()      
    answer = len(cards)
    
    for i in range (len(cards)) :
      if cards[i] in table :
        answer = min(answer, i - table[cards[i]])
      table[cards[i]] = i
      
    if answer == len(cards) : answer = -2
    
    return answer + 1