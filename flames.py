# Structure for a Node implemented as a class
class Node:
	
	# Constructor for class Node
	def __init__(self, data):
		self.data = data
		self.next = None

class NameStriker:
	def strike(self, boyName, girlName):
		boyName = boyName.lower()
		girlName = girlName.lower()
		
		i = 0
		j = 0
		strikeCount = 0
		whiteSpaceCount = 0
		while i < len(boyName):
			j = 0
			while j < len(girlName):
				if boyName[i] is ' ':
					#ignore whitespace
					a = 1
				elif boyName[i] is girlName[j]:
					girlName = girlName[:j] + '*' + girlName[j+1:]
					strikeCount += 2
					j = j + 1		
					break
				j = j + 1
			i = i + 1

		strikeCount = len(boyName) + len(girlName) - strikeCount - (boyName.count(' ') + girlName.count(' '))
		return strikeCount

	def flamesCalculate(self, boyName, girlName):
		flamesList = ['FRIENDS', 'LOVE', 'AFFECTIONATE', 'MARRIAGE', 'ENEMIES', 'SIBLINGS']
		strikeCount = NameStriker.strike(self, boyName, girlName)
		p = fNode = Node(flamesList[0])
		i = 1
		for i in range(1, 6):
			p.next = Node(flamesList[i])
			p = p.next

		p.next = fNode

		count = 6
		while count > 0:
			for i in range(0, (strikeCount-1)):
				p = p.next
			
			p.next = p.next.next
			count = count - 1
		
		return p.data
