class Solution(object):
    def solution_575_3(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
		# Calculate the total value each list should satisfy
        alice, bob = 0, 0
        for i in aliceSizes: alice += i
        for j in bobSizes: bob += j
        each = (alice+bob)/2
		# Sort each list first to utilize the binary search
        aliceSizes.sort()
        bobSizes.sort()
        for i in range(len(aliceSizes)):
            alice_change = aliceSizes[i]
            bl, br = 0, len(bobSizes)-1
            while bl <= br:
                bm = bl + (br-bl)//2
                bob_change = bobSizes[bm]
                new_alice = alice - alice_change + bob_change
                new_bob = bob + alice_change - bob_change
				# If two list have the same value, then break
                if new_alice == new_bob:
                    return [alice_change, bob_change]
                    break
				# If new_alice > new_bob, we should choose a larger value for exchanging
                elif new_alice > new_bob:
                    br = bm - 1
				# If new_alice < new_bob, we should choose a smaller value for exchanging
                elif new_alice < new_bob:
                    bl = bm + 1