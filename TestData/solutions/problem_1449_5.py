class Solution:
    def solution_1449_5(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []                                             // Store the possible recipes
        dict1 = {}                                          //Map each recipe to its ingredient
        supplies = set(supplies)                   //Converting to set in order to store unique supplies and avoid redundant checks
        for i in range(len(recipes)):
            dict1[recipes[i]] = ingredients[i]  //Map each recipe to its ingredient
        while True:                                       // loop until terminating criteria is reached
            temp = []                                    //temp array to store the non-possible reciepes for a particular iteration
            for i in range(len(recipes)):         //Iterage the reciepe array
                flag = True                             // Assume each recipe is possible in the start
                for j in range(len(dict1[recipes[i]])):          //iterate each ingredient for each reciepe
                    if dict1[recipes[i]][j] not in supplies:     // and check if its available in supplies
                        flag = False                                       //if not available then set the flag to false
                        temp.append(recipes[i])                   //and add the not possible(maybe as of now) reciepe to temp array
                        break                                                   //and break
                if flag:                                                          //if the reciepe is possible
                    ans.append(recipes[i])                             //then add the reciepe to ans array
                    supplies.add(recipes[i])                           //also add the reciepe to the supply array as it is possible
            if temp == recipes:                                         //terminating criteria for while True loop if there is no change in temp array then break
                break
            else:
                recipes = temp                                            // else update the reciepes array with temp
        return ans                                                          //Lastly return the ans