class Solution:
    def solution_779_2(self, transactions: List[str]) -> List[str]:
        hashmap = {}
		#Hashset is used to skip redudant transactions being added to the result
		#We will only store index of the transaction because the same transaction can repeat.
        result = set()
        for i, t in enumerate(transactions):
            name, time, amount, city =  t.split(",")
			#If there is no transaction record for the user
            if name not in hashmap:
                hashmap[name] = []
                if int(amount) > 1000:
                    result.add(i)
			#If there are pass transaction records
            else:
				#Fetching past transaction from hashmap
                prevTrans = hashmap[name]
				#Iterating over the past transaction of the user and finding anomalies
                for j in range(len(prevTrans)):
                    prevName, prevTime, prevAmount, prevCity = transactions[prevTrans[j]].split(",")
                    #Checking whether the amount exceeds $1000
					if int(amount) > 1000:
                        result.add(i)
					#Checking whether it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
                    if abs(int(time) - int(prevTime)) <= 60 and city != prevCity:
                        result.add(i)
                        result.add(prevTrans[j])
			#Recording transaction in the hashmap for the user
            hashmap[name].append(i)
		
		#Fetching transaction using indexes stored in the result set and returning
        return [transactions[t] for t in result]