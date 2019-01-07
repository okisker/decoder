import enchant
import binascii

x = input('type test word here: ') 

#SPELLCHECK FUNCTION
def spellcheck(x):
	from enchant.checker import SpellChecker
	checker = SpellChecker("en_US")
	checker.set_text(x)

	#IF ONLY NUMBERS
	allowed_chars = set('0123456789 ')
	if set(x).issubset(allowed_chars):
		return ('this text is probably not english: '+x)

	#IF NOT ENGLISH WORDS
	for err in checker:
		return ('this text is probably not english: '+err.word)
		break

	#IF ENGLISH WORDS
	else:
		return("english word(s) detected!")

#CALL SPELLCHECK FUNCTION ON ORIGINAL INPUT x
print (spellcheck(x))



#IDENTIFY TEXT- WHAT KIND OF CODE IS IT

#IF BINARY
allowed_chars = set('10 ')
if set(x).issubset(allowed_chars):
	print ("this text is binary")

	#TRANSLATE BINARY TO TEXT FUNCTION
	def binfun(x):
		#REMOVE SPACES
		x = x.replace(" ","")
		#DECODE
		n = int(x, 2)
		return(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

	#CALL FUNCTION & PRINT
	binx = binfun(x)
	print('BINARY DECODED AS: "'+binx+'"')
	#CHECK AGAINST SPELL CHECKER
	print(spellcheck(binx))

else:
	print ("this text is probably not binary")

#IDENTIFY TEXT- WHAT KIND OF CODE IS IT

#IF CAESAR CIPHER
#BRUTE FORCE CODE
def caesarciph(x):
	message = x.upper()
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for key in range(len(LETTERS)):
		translated = ''
		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol) # get the number of the symbol
				num = num - key

				if num < 0:
					num = num + len(LETTERS)

				translated = translated + LETTERS[num]
			else:
				translated = translated + symbol
		#print('Key #%s: %s' % (key, translated))
		response = spellcheck(translated)
		if response == 'english word(s) detected!':
			print('CAESAR CIPHER DECODED AS: "'+translated+'"')
			break
		elif key == 25 and response != 'english word(s) detected!':
			print("this text is probably not caesar cipher")
	return

caesarciph(x)	