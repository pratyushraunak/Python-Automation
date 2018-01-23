#######################################################################################################################
# Pratyush Raunak												       #
# Python Automation 												       #
# Decode this - 667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268				       #
# The above string is encoded by hex values, encrypted using Caesar Cipher (Key = 3), and ordinal value is xored by ^10#
########################################################################################################################

import string	#importing the string module

def plain(n):
	upper = string.ascii_uppercase #contains only the uppercase letters
	lower = string.ascii_lowercase #contains only the lowercase letters
	digits = string.digits #contains numbers

	my_list = [] #new list
	key = int(raw_input("enter the key:")) #user input key length
	
	for i in n: #iiterating over the user input string (n)
		if i.isupper() is True: #checking if i is upper or not
			my_list.append(upper[(upper.index(i) - key) %26]) #plaintext = (message - key)%26
		elif i.islower() is True:
			my_list.append(lower[(lower.index(i) - key) %26])
		elif i.isdigit() is True:
			my_list.append(digits[(digits.index(i) - key) %10]) #plaintext = (digit - key)%10
	
	return  my_list

def un_xor(x):
	return "".join(chr(ord(i)^10) for i in x) #Un-Xoring, if c = a ^ b then a = c ^ b and b = c ^ a method


def decode_my(y):
	return y.decode('hex') # hex value to ascii


message = raw_input("enter the message:") #user input string 
plain_text = plain(un_xor(decode_my(message))) #caalling all the three functions
plain_text = "".join(plain_text) #joining the list values
print plain_text #printing the final palintext
