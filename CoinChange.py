#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class CoinChange:

	def NumberofCoins(self,denomination,value):
		 #Write your code here to find out minimum number of coins required to provide the change for given value.
		 #This method will have a denomination array and an int which specifies the value as inputs(Please see testcase file)
		 #This method should return the number of coins
		table = [ float('inf') for i in range(value + 1)]
		table[0] = 0
		for i in range(1, value + 1):
			for d in denomination:
				if d <= i:
					table[i] = min(table[i], table[ i - d ] + 1)
				else:
					break
		return table[value]
		
		 


