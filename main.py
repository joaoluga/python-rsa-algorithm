import sys
sys.setrecursionlimit(5000)
from datetime import datetime
from rsa import Rsa

message = "The information security is of great importance to ensure the privacy of communications"

# Testing performance with prime numbers with more than 100 digits
# rsa_code = Rsa()
# for x in range(100,1100,100):
# 	rsa_code = Rsa()
# 	print('Digits: {}'.format(x))
# 	rsa_code.key_gen(message=message, digits=x)
# 	print('Performance: {}\n\n'.format(rsa_code._performance))	


rsa_code = Rsa()
start = datetime.now()
rsa_code.key_gen(message=message, digits=30)
total_time = (datetime.now() - start).total_seconds()

print('Message: {}\n'.format(rsa_code._message))
print('Public key: {}\n'.format(rsa_code._public_key))
print('Private Key: {}\n'.format(rsa_code._private_key))
print('p: {}'.format(rsa_code._p))
print('q: {}\n\n'.format(rsa_code._q))
print('Encode: {}\n\n'.format(rsa_code._encode))
print('Decode: {}'.format(rsa_code._decode))
print('Performance: {}'.format(rsa_code._performance))
print('Total seconds: {}'.format(total_time))
