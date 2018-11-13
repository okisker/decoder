import enchant

x = input('type test word here:' ) 

from enchant.checker import SpellChecker
checker = SpellChecker("en_US")
checker.set_text(x)
for err in checker:
	print ("ERROR:", err.word)
