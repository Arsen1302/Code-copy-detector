class Solution:
	def solution_726_5(self, words: List[str]) -> int:
		words.sort(key=len)
		dp = {}
		for word in words:
			for i in range(len(word)):
				if word not in dp:
					dp[word]=dp.get(word[:i]+word[i+1:],0)+1
				else:
					dp[word]=max(dp.get(word[:i]+word[i+1:],0)+1,dp[word])
		return max(dp.values())