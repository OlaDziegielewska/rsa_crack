from rsa_crack import * 
if __name__  == "__main__":
	# Wiener
	attack = CRsa_Wiener(17993, 90581)
	wiener_base = attack.run()
	print("[*] Wiener: Found private {}".format(wiener_base.d))
	# Factor
	mRsa = CRsa_Factor();
	mBase = mRsa.Crack(10,89*97);
	print '[*] Factor: mBase: ',mBase.m_iE,' ',mBase.m_iN
	print '[*] Factor: mBase q: ',mBase.m_iQ
	print '[*] Factor: mBase p: ',mBase.m_iP
