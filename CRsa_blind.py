import random, math
from CRsa_Base import CRsa_Base											


class CRsa_blind(CRsa_Base):	
	
	
	def rand_blind(self):
		g = xgcd(self.m_iE, self.m_iN)[0]
		rand = random.randrange(2,self.m_iN)
		while g != 1:
			rand = random.randrange(2,self.m_iNn)
			g=xgcd(self.m_iE,self.m_iN)[0]
		return rand	


	def Blind_File(self,path):
			with open(path, 'r') as myfile:
				data = myfile.read()
				string_a = ''

				for ch in data:
					ch_a = ord(ch)
					string_a += str(ch_a)
				string_int = int(string_a)
				print "Plik tekstowy o tresci: " + data
				r = self.rand_blind()
				print "wartosc r " + str(r)
				m = (string_int * pow(r,self.m_iE))%self.m_iN			
				print "wartosc m " + str(m)
				blinded_f = open("Blinded.txt", "w")
				blinded_f.write(str(m))
				blinded_f.close()
				r_f = open("random_value.txt", "w")
				r_f.write(str(r))
				r_f.close()


	def Sign(self):
		with open('Blinded.txt', 'r') as myfile:
			 data = myfile.read()
			 s = (pow(int(data),self.m_iD))%self.m_iN
			 print "wartosc s' " + str(s)
			 signed_f = open("Signed.txt", "w")
			 signed_f.write(str(s))
			 signed_f.close()


	def Remove_Blinding(self):
		with open("Signed.txt",'r') as myfile, open("random_value.txt",'r') as r:
			data = myfile.read()
			rv = r.read()
			s = int(data)*modinv(int(rv),self.m_iN)%self.m_iN
			print "wartosc s " + str(s)
			fake_f = open("Fake_sign.txt", "w")
			fake_f.write(str(s))
			fake_f.close()

	def Check(self):
		with open("Test.txt",'r')as myfile:
			data = myfile.read()
			string_a =''
			
			for ch in data:
				ch_a = ord(ch)
				string_a += str(ch_a)
			string_int = int(string_a)
			
			s = (pow(string_int,self.m_iD))%self.m_iN					
			print "sprawdzenie s " + str(s)
			signed_f = open("Check.txt", "w")
			signed_f.write(str(s))
			signed_f.close()
