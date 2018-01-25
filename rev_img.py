#######################################################################################################################
# Pratyush Raunak												       #
# Python Automation 												       #
# Fixing the reversed bytes and nibbles to construct an image.							       #
# 														       #
########################################################################################################################

def read_file():
	with open("reverse", "rb") as binary_file: #opening the file to read as byte
		data = binary_file.read()
		data = bytearray(data)
		data = data[::-1] #reversing the entire byte sequence
		rev_nibble(data) #function call
def rev_nibble(data):
	 swap_data='' #intializing a variable
	 for i in data:
		low_nibble = i & 0x0F #getting low nibble value
    		high_nibble = i & 0xF0 #getting high nibble value 
    		result = (high_nibble >> 4) | (low_nibble << 4) #swapping the nibbles and joining the nibble as one byte

		swap_data+=chr(result)
		out_file(swap_data)


def out_file(swap_data):
	with open("my_rev_img.png", "wb") as outfile: #writing bytes to a file
		 outfile.write(str(swap_data))

read_file()

