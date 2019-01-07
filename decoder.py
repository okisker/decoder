import enchant
import binascii

x = input('type test word here: ' ) 

def spellcheck(x):
	from enchant.checker import SpellChecker
	checker = SpellChecker("en_US")
	checker.set_text(x)
	for err in checker:
		print ("ERROR NOT ENGLISH WORD:", err.word)	
	return

# identify text- what kind of code is it
# if binary
allowed_chars = set('10 ')
if set(x).issubset(allowed_chars):
	print ("this text is binary")

	# translate binary to text
	def binfun(x):
		#remove spaces
		x = x.replace(" ","")
		n = int(x, 2)
		return(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
	newx = binfun(x)
	print("BINARY DECODED AS: \"",newx,"\"")
	# check against spell checker
	print(spellcheck(newx))
else:
	print ("this text is probably not binary")
	