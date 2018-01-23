import string

def plain(n):
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	digits = string.digits

	my_list = []
	key = int(raw_input("enter the key:"))
	
	for i in n:
		if i.isupper() is True:
			my_list.append(upper[(upper.index(i) - key) %26])
		elif i.islower() is True:
			my_list.append(lower[(lower.index(i) - key) %26])
		elif i.isdigit() is True:
			my_list.append(digits[(digits.index(i) - key) %10])
	#my_list = my_list.replace('0', '')
	#print my_list
	return  my_list

def un_xor(x):
	#print x
	#for i in x:
		#my_text = "".join(chr(ord(chr(ord(i)))^10))
        #print "".join(chr(ord(chr(ord(i)))^10)for i in x)
	return "".join(chr(ord(i)^10) for i in x)


def decode_my(y):
	#y = y.replace('<','')
	#y = y.strip()
	#print y
	return y.decode('hex')


message = raw_input("enter the message:")
#plain_text = decode_my(un_xor(plain(message)))
plain_text = plain(un_xor(decode_my(message)))
plain_text = "".join(plain_text)
print plain_text
