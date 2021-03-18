import pysubs2
import sys
from googletrans import Translator
arg=sys.argv[0]
translator = Translator()
subs= pysubs2.load(sys.argv[1], encoding="utf-8")
for line in subs :
	if line.text.find("{") == -1   :
		if line.text.find(r"\N")== -1 :
		    line.text = translator.translate(line.text,dest='ar').text
		else:
			pos= line.text.find(r"\N")
			line.text = translator.translate(line.text[:pos-1],dest='ar').text + r"\N"+ translator.translate(line.text[pos+1:],dest='ar').text
	else :
	    pos = line.text.find("}")
	    line.text = translator.translate(line.text[pos+1:],dest='ar').text

subs.save(sys.argv[2])

