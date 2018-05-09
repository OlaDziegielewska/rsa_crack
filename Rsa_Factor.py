

import random
from CRsa_Base import CRsa_Base

class CRsa_Factor(object):
	def Test(self):
		print 'Wywolana funkcja klasy'
	def Crack(self,e,n):
		print 'Wywolana funkcja klasy',e,' ',n
		
		mBase = CRsa_Base();
		mBase.m_iE = e;
		mBase.m_iN = n;

		if not n%2:
			mBase.m_iP = 2;
			mBase.m_iQ = n/mBase.m_iP;
			return mBase;
		if not n%3:
			mBase.m_iP = 2;
			mBase.m_iQ = n/mBase.m_iP;
			return mBase;

		
		i = 5;
		while (i*i) < n:
		
			if not n%i:
				break
		
			if not n%(i+2):
				i = i+2;
				break;
			i += 6;
			


		mBase.m_iP = i;
		mBase.m_iQ = n/mBase.m_iP;

		return mBase;







mRsa = CRsa_Factor();
mBase = mRsa.Crack(10,89*97);

print 'mBase: ',mBase.m_iE,' ',mBase.m_iN
print 'mBase q: ',mBase.m_iQ
print 'mBase p: ',mBase.m_iP
