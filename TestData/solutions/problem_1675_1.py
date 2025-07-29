class Solution:                   # Ex: names = ["Larry","Curly","Moe"]   heights = [130,125,155] 

    def solution_1675_1(self, names: List[str], heights: List[int]) -> List[str]:

        _,names = zip(*sorted(zip(heights,names), reverse = True))   
                                  # zipped   --> [(130,"Larry"), (125,"Curly"), (155,"Moe")  ]
                                  # sorted   --> [(155,"Moe"  ), (130,"Larry"), (125,"Curly")]
                                  # unzipped --> _ = (155,130,125) , names = ("Moe","Larry","Curly")
        
		return  list(names)       # list(names) = ["Moe","Larry","Curly"]