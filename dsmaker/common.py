

class Dictionary:
	def __init__(self, path):
		self.load(path)

	def load(self, path):
		self.data = {}
		self.clss = {}
		for line in open(path):
			entry = line.strip().split()
			
			name = entry[0]
			type = int(entry[1])
			id = int(entry[2])
			
			if type:
				self.data[id] = (name, type)
			else:
				self.clss[id] = name
			
	def _(self, id, default = 0):
		try:
			entry = self.data[id]
			return (entry[0], entry[1], self.clss[entry[1]])
		except:
			return default

	def id(self, name,default = ""):
		try:
			return [id for id, entry in self.data.items() if entry[0] == name][0]
		except:
			return default

