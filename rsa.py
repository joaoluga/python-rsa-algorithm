#custom
from miller_rabin import MillerRabinPrimalityTest 
#bult-in
import random
from math import gcd as bltin_gcd
from datetime import datetime

class Rsa(object):

	def __init__(self, message=None, p=None, q=None):
		self._message = message
		self._p = p
		self._q = q
		self._N = None
		self._Ntot = None
		self._e = None
		self._d = None
		self._public_key = None
		self._private_key = None
		self._encode = ''
		self._encode_list = []
		self._decode_list = []
		self._decode = ''
		self._coprime_result = None
		self._performance = {}

	@staticmethod
	def prime_number(digits):

		check_if = MillerRabinPrimalityTest()
		b = False
		while b == False:
			n1 = random.randrange(start=int('1'+'0'*(digits-1)),stop=int('9'*(digits)))
			b = check_if.is_prime(n=n1, _precision_for_huge_n=16)
		return n1

	@staticmethod
	def coprime(a, b):
		return bltin_gcd(a, b) == 1

	def eea(self,a,b):
		if b==0:return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = self.eea(b,r)
		return (t, s-(q*t) )
	
	def find_inverse(self,x,y):
		inv = self.eea(x,y)[0]
		if inv < 1: inv += y
		return inv

	def msg_encode(self, message, e, N):
		self._encode_list = list(map(lambda x: pow(ord(x),e,N), list(message)))
		self._encode = self._encode.join(str(value) for value in self._encode_list)

	def msg_decode(self, encode, d, N):
		self._decode_list = list(map(lambda x: chr(pow(x,d,N)), encode))
		self._decode = self._decode.join(str(value) for value in self._decode_list)

	def key_gen(self, message, digits):

		start_key_gen = datetime.now()
		start = datetime.now()
		if self._message == None:
			self._message = message
		self._performance['_message'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		if self._p == None:
			self._p = self.prime_number(digits)
		self._performance['_p'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		if self._q == None:
			self._q = self.prime_number(digits)
		self._performance['_q'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		self._N = self._p*self._q
		self._performance['_N'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		self._Ntot = (self._p-1)*(self._q-1)
		self._performance['_Ntot'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		self._coprime_result = False
		while self._coprime_result == False:
			self._e = random.randrange(start=2,stop=self._Ntot-1)
			self._coprime_result = self.coprime(self._e,self._Ntot)
		self._performance['_e'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		self._d = self.find_inverse(self._e, self._Ntot)
		self._performance['_d'] = (datetime.now() - start).total_seconds()

		self._public_key = [self._e, self._N]
		self._private_key = [self._d, self._N]

		start = datetime.now()
		self.msg_encode(self._message, self._e, self._N)
		self._performance['_encode'] = (datetime.now() - start).total_seconds()

		start = datetime.now()
		self.msg_decode(self._encode_list, self._d, self._N)
		self._performance['_decode'] = (datetime.now() - start).total_seconds()
		self._performance['key_gen'] = (datetime.now() - start_key_gen).total_seconds()
