

import random
from CRsa_Base import CRsa_Base

class CRsa_Factor(object):
	def Test(self):
		pass
	def Crack(self,e,n):
		
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




