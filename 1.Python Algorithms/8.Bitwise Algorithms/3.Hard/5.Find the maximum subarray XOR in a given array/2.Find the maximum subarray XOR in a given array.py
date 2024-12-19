"""Python implementation for a Trie based solution
to find max subArray XOR"""

"""structure of Trie Node"""
class Node:

	def __init__(self, data):

		self.data = data
		self.left = None # left node for 0
		self.right = None # right node for 1

""" class for implementing Trie """

class Trie:

	def __init__(self):

		self.root = Node(0)

	"""insert pre_xor to trie with given root"""
	def insert(self, pre_xor):

		self.temp = self.root

		"""start from msb, insert all bits of pre_xor
		into the Trie"""
		for i in range(31, -1, -1):

			"""Find current bit in prefix sum"""
			val = pre_xor & (1<<i)

			if val :
				"""create new node if needed"""
				if not self.temp.right:
					self.temp.right = Node(0)
				self.temp = self.temp.right

			if not val:
				"""create new node if needed"""
				if not self.temp.left:
					self.temp.left = Node(0)
				self.temp = self.temp.left

		"""store value at leaf node"""
		self.temp.data = pre_xor

	"""find the maximum xor ending with last number
		in prefix XOR and return the XOR of this"""
	def query(self, xor):

		self.temp = self.root

		for i in range(31, -1, -1):

			"""find the current bit in prefix xor"""
			val = xor & (1<<i)

			"""Traverse the trie, first look for opposite bit
				and then look for same bit"""
			if val:
				if self.temp.left:
					self.temp = self.temp.left
				elif self.temp.right:
					self.temp = self.temp.right
			else:
				if self.temp.right:
					self.temp = self.temp.right
				elif self.temp.left:
					self.temp = self.temp.left

		return xor ^ self.temp.data

	"""returns maximum XOR value of subarray"""
	def maxSubArrayXOR(self, n, Arr):

		"""insert 0 in the trie"""
		self.insert(0)

		"""initialize result and pre_xor"""
		result = -float('inf')
		pre_xor = 0

		"""traverse all input array element"""
		for i in range(n):

			"""update current prefix xor and insert it into Trie"""
			pre_xor = pre_xor ^ Arr[i]
			self.insert(pre_xor)

			"""Query for current prefix xor in Trie and update result"""
			result = max(result, self.query(pre_xor))

		return result

"""Driver program to test above functions"""
if __name__ == "__main__":

	Arr = [8, 1, 2, 12]
	n = len(Arr)
	trie = Trie()
	print(trie.maxSubArrayXOR(n, Arr))

# This code is contributed by chaudhary_19
