

def read_file():
	with open("reverse", "rb") as binary_file:
		data = binary_file.read()
		data = bytearray(data)
		data = data[::-1]
		rev_nibble(data)
def rev_nibble(data):
	 swap_data=''
	 for i in data:
		low_nibble = i & 0x0F
    		high_nibble = i & 0xF0
    		result = (high_nibble >> 4) | (low_nibble << 4)

		swap_data+=chr(result)
		out_file(swap_data)


def out_file(swap_data):
	with open("my_rev_img.png", "wb") as outfile:
		 outfile.write(str(swap_data))

read_file()

