class Person():
	def __init__(self, name, pref):
		self.name = name
		self.pref = pref
		self.oPartner = None
		self.partnerOrder= None
		self.OExPartner = None

	def marry(self, oPartner):
		self.oPartner = oPartner
		oPartner.oPartner = self

		print (self.name + " got married with "+ oPartner.name)

	def divorceAndMarry(self, oNewPartner):
		OExPartner = self.oPartner

		self.OExPartner = OExPartner
		OExPartner.oPartner = None

		print (OExPartner.name + " is now alone")

		oNewPartner.marry(self)

	def propose(self, oNewPartner):
		if oNewPartner.oPartner:

			if oNewPartner.pref[oNewPartner.oPartner.name] < oNewPartner.pref[self.name]:
				oNewPartner.divorceAndMarry(self)
				
			else:
				print(oNewPartner.name + " refuses to marry " + self.name)

		else:
			self.marry(oNewPartner)

prefV = {'B':5, 'A':4, 'D':3, 'E':2, 'C':1}
prefW = {'D':5, 'B':4, 'A':3, 'C':2, 'E':1}
prefX = {'B':5, 'E':4, 'C':3, 'D':2, 'A':1}
prefY = {'A':5, 'D':4, 'C':3, 'B':2, 'E':1}
prefZ = {'B':5, 'D':4, 'A':3, 'E':2, 'C':1}

prefA = {'Z':5, 'V':4, 'W':3, 'Y':2, 'X':1}
prefB = {'X':5, 'W':4, 'Y':3, 'V':2, 'Z':1}
prefC = {'W':5, 'X':4, 'Y':3, 'Z':2, 'V':1}
prefD = {'V':5, 'Z':4, 'Y':3, 'X':2, 'W':1}
prefE = {'Y':5, 'W':4, 'Z':3, 'X':2, 'V':1}

oV = Person("V", prefV)
oW = Person("W", prefW)
oX = Person("X", prefX)
oY = Person("Y", prefY)
oZ = Person("Z", prefZ)

oA = Person("A", prefA)
oB = Person("B", prefB)
oC = Person("C", prefC)
oD = Person("D", prefD)
oE = Person("E", prefE)

oV.partnerOrder = [oB, oA, oD, oE, oC]
oW.partnerOrder = [oD, oB, oA, oC, oE]
oX.partnerOrder = [oB, oE, oC, oD, oA]
oY.partnerOrder = [oA, oD, oC, oB, oE]
oZ.partnerOrder = [oB, oD, oA, oE, oC]

oA.partnerOrder = [oZ, oV, oW, oY, oX]
oB.partnerOrder = [oX, oW, oY, oV, oZ]
oC.partnerOrder = [oW, oX, oY, oZ, oV]
oD.partnerOrder = [oV, oZ, oY, oX, oW]
oE.partnerOrder = [oY, oW, oZ, oX, oV]

boys=[oV,oW,oX,oY,oZ]

def boyProposesToNewGirl(boy, firstGirlOnTheList):
	boy.partnerOrder.remove(firstGirlOnTheList)
	boy.propose(firstGirlOnTheList)

for boy in boys:

	boy.propose(boy.partnerOrder[0])

	while boy.oPartner is None:
		boyProposesToNewGirl(boy, boy.partnerOrder[0])

	exHusband = boy.partnerOrder[0].OExPartner

	if exHusband:

		while exHusband.oPartner is None:
			boyProposesToNewGirl(exHusband, exHusband.partnerOrder[0])

	else:

		while boy.oPartner is None:				
			boyProposesToNewGirl(boy, boy.partnerOrder[0])
			exHusband = girl.OExPartner

			while exHusband.oPartner is None:
				boyProposesToNewGirl(boy, boy.partnerOrder[0])