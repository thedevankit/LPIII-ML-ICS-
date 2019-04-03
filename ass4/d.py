# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
# -*- coding: encoding -*-
from __future__ import print_function
# Variables Used
sharedPrime = 23
sharedBase = 5
aliceSecret = 6
bobSecret = 15
# Begin
print( "Publicly Shared Variables:")
print( "Publicly Shared Prime: " , sharedPrime )
print( "Publicly Shared Base: " , sharedBase )

# Alice Sends Bob A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print  ("\n Alice Sends Over Public Chanel: " , A )

# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print(" \n Bob Sends Over Public Chanel: ", B )

print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "Alice Shared Secret: ", aliceSharedSecret )

bobSharedSecret = (A**bobSecret) % sharedPrime
print( " Bob Shared Secret: ", bobSharedSecret )
##########################OUTPUT############################
#chanchald@chanchald-X553SA:~$ cd Desktop
#chanchald@chanchald-X553SA:~/Desktop$ python d.py
#Publicly Shared Variables:
#Publicly Shared Prime:  23
#Publicly Shared Base:  5

# Alice Sends Over Public Chanel:  8
 
# Bob Sends Over Public Chanel:  19

#------------

#Privately Calculated Shared Secret:
#Alice Shared Secret:  2
# Bob Shared Secret:  2
#chanchald@chanchald-X553SA:~/Desktop$ 

