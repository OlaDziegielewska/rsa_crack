class CRsa_Base():
	
	def __init__(self, e = 0, n = 0, p = 0, q = 0, d = 0):
		self.m_iN = n
		self.m_iE = e
		self.m_iP = p
		self.m_iQ = q
		self.m_iD = d

