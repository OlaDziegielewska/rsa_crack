import gmpy2
import binascii
import math
import sys

from Crypto.PublicKey import RSA


'''

Hastad’s Broadcast Attack is a mathematical approach to recover the secret message that encrypted using RSA with multiple different moduli numbers known as n1, n2, n3,…, ni and a single small public exponent e. This attack is based on Chinese Remainder Theorem(CRT) that said if all the moduli are relatively prime, we can compute x such as x ≡ y1 (mod n1), x ≡ y2 (mod n2), x ≡ y3 (mod n3). 

'''



#Example data to check work of our module


'''
e = 3
c1 = gmpy2.mpz("261345950255088824199206969589297492768083568554363001807292202086148198677263604958247638518239089545015544140878441375704999371548235205708718116265184277053405937898051706510050325657424248032017194168466912140157665066494528590260879287464030275170787644749401275343677539640347609231708327119700420050952")
n1 = gmpy2.mpz("1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627")
c2 = gmpy2.mpz("147535246350781145803699087910221608128508531245679654307942476916759248448374688671157343167317710093065456240596223287904483080800880319712443044372346198448258006286828355244986776657425121775659144630571637596283100201930037799979864768887420615134036083295810488407488056595808231221356565664602262179441")
n2 = gmpy2.mpz("405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309")
c3 = gmpy2.mpz("633230627388596886579908367739501184580838393691617645602928172655297372282390454586345936209841638502749645277206386289490247066959822668419069562380546618337543323956757811325946190976649051724173510367477564435069180291575386473277111391106753472257905377429144209593931226163885326581862398737742032667573")
n3 = gmpy2.mpz("1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723")
'''



# class to get the primal components from file with public key

class PublicKey():
	def __init__(self, path):
		self.n = None
		self.e = None
		self.path = path
		self.key = None
	# Importuj klucz z pliku
	def importkey(self):
		f = open(self.path, 'r')
		self.key = RSA.importKey(f.read())
		f.close()
		self.n = self.key.n
		self.e = self.key.e
		

# function to convert binary message to decimal value

def parseCrip(self):
	f = open(self, 'r+')
	crip = int(binascii.b2a_hex(f.read()),16)
	f.close()
	
	return crip


# the hastad attack

def  hastadAttack(n1,n2,n3,c1,c2,c3):
	e=3
	M = n1*n2*n3
	m1 = M/n1
	m2 = M/n2
	m3 = M/n3
	t1 = c1*(m1)*gmpy2.invert(m1,n1)
	
	t2 = c2*(m2)*gmpy2.invert(m2,n2)
	t3 = c3*(m3)*gmpy2.invert(m3,n3)
	print ("t3 = {}".format(t3))
	print "\n" 
	x = (t1+t2+t3) % M # chinese reminder theorem
	print ("x = {}".format(x))
	print "\n" 
	m, exact = gmpy2.iroot(x,e) # recover m

	print exact
	if exact:
		
	    	print binascii.unhexlify(gmpy2.digits(m,16)) # convert int -> hex -> ascii








