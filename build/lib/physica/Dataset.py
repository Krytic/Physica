class Dataset:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def me(self):
		print(self.x)
		print(self.y)
		print(np.arange(3))