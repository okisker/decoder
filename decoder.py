import enchant
#d = enchant.Dict("en_US")
#from enchant.checker import spellcheck

x = input('type test word here:' ) 
#d.check(x)

from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")
chkr.set_text(x)
for err in chkr:
	print ("ERROR:", err.word)
