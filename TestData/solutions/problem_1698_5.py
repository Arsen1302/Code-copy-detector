class Solution:
    def solution_1698_5(self, event1: List[str], event2: List[str]) -> bool:
        
        arr = [[(int(event1[0][:2])*60)+int(event1[0][3:]) , (int(event1[1][:2])*60)+int(event1[1][3:])] ,
               [(int(event2[0][:2])*60)+int(event2[0][3:]) , (int(event2[1][:2])*60)+int(event2[1][3:])]]
        
        return (arr[0][0] <= arr[1][1] <= arr[0][1] or
                arr[1][0] <= arr[0][1] <= arr[1][1])