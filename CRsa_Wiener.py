import math
import sys
from gmpy2 import *
from CRsa_Base import CRsa_Base

"""
	This module tries to find private key exponent for a given public exponent e and modulus n using Wiener attack.
		
	The attack uses the continued fraction method to expose the private key d when d is small.
	Wiener has proved that the attacker may efficiently find d when d < (n^1/4)/3.
	
	Continued fractions from wikipedia:
		In mathematics, a continued fraction is an expression obtained through an iterative process of representing a number as the sum of its integer part and the reciprocal of another number, then writing this other number as the sum of its integer part and another reciprocal, and so on.


	How attack works:
	We now that:
		d*e=1mod(fi(n)), so
		d*e=kfi(n)+1
	
		fi(n)=(p-1)(q-1)=p*q-(p+q)+1
		p*q is huge number so we assume that p*q - (p+q) is approximate equal n.
 
		d*e - kfi(n) = 1
		Now we approximate fi(n) to n:
		d*e - k*n = 1
		Divied by n*d
	
		(e/d) - (k/d) = 1/(n*d)
		
		1/(n*d) should be small number. So again we assume that	(e/n) is approcimate equel  (k/d)
		In first step we try to find the continued fractions expansion of e/n.
		Next we calcute convergants k/d based on fractions of e/n. Then for each convergent we check if it produces factorizaton of n.
		In order to that we solve equation:
			x^2 - ((n-fi(n))+1)x+n=0, where fi(n) = (ed-1)/k

	d - private exponent
	e - public exponent
	n - modulus n
	p - prime number
	q - prime number

	Methods:
		CRsa_Wiener.ContinuedFractions(e, n)		
			Returns the continued fractions expansion of e/n.  	
		CRsa_Wiener.CalcConvergents(fractions)
			Based on fractions calculates and returns convergents k/d. Where variable fractions is list [k1,k2,...,kn].
		CRsa_Wiener.FindKey(e, n, convergents)
			Finds and returns valid convergent. Calls CRsa_Wiener.Check method in order to check if convergent is valid.
		CRsa_Wiener.Check
			Checks if convergent is valid. Returns True if is valid and False if is not.
"""


class CRsa_Wiener():
	def __init__(self, e, n):
		self.mBase = CRsa_Base()
		self.mBase.e = e
		self.mBase.n = n
		
		
	def run(self):

		fractions = self.ContinuedFractions(self.mBase.e, self.mBase.n)

		convergents = self.CalcConvergents(fractions)

		self.mBase.d = self.FindKey(self.mBase.e, self.mBase.n, convergents)
		if self.mBase.d:
			return self.mBase

		return None

	

	def ContinuedFractions(self, e, n):
		r = 0
		temp = 0
		fractions = []
		while n != 0:
			r = e//n
			temp = e%n
			e = n
			n = temp
			fractions.append(r)	

		return fractions

	def CalcConvergents(self, fractions):

		convergents = []
		temp = []

		for i in range(1, len(fractions)+1):
			temp = fractions[0:i]
			k = temp[-1]
			d = 1
			for j in range(-2, -i-1, -1):
				# b + c/a = (b*a + c) / a
				k,d = temp[j]*k + d, k
					
			convergents.append((k, d))

		return convergents

	def FindKey(self, e, n, convergents):
		for convergent in convergents:
			if self.Check(e, n, convergent[0], convergent[1]):
				return convergent[1]
		return None


	def Check(self, e, n, k, d):

		if (k == 0) or (d % 2 == 0) or d==1:
			return False

		if not((e*d-1) % k == 0):
			return False
		phi = long((e*d-1)/k)

		b = long(n - phi + 1)
		delta = long(b*b - 4*n)
		if delta >= 0:
			vdelta = isqrt(mpz(delta))
			if not ((( -b - vdelta) % 2 == 0) and ((-b + vdelta) % 2 ==0)):
				return False
			self.mBase.p = abs(long((-b - vdelta)/2))
			self.mBase.q = abs(long((-b + vdelta)/2))
			return True

		return False
			 

