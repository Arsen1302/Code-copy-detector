class Solution:
    def solution_1232_4_1(self, sentence1: str, sentence2: str) -> bool:
        s2 = sentence2.split(' ')
        s1 = sentence1.split(' ')
        
        def solution_1232_4_2(s1,s2):
            idx = 0
            for i in range(len(s2)):
                if s2[i] == s1[i]:
                    idx+=1
                else:
                    break
         
            left = s2[idx:]
            itemTake = len(s2)-idx
            right = s1[len(s1)-itemTake:]
            return ' '.join(left) == ' '.join(right)

            ## alternative way to save memory
            ## for i in range(idx, len(s2)):
            ##      if s2[i] != s1[len(s1)-len(s2)+i]:
            ##          return False
            ##      return True
            

        if len(s1) > len(s2):
            return solution_1232_4_2(s1,s2)
        else:
            return solution_1232_4_2(s2,s1)