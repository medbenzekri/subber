import pysubs2
import sys
from googletrans import Translator

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()




arg=sys.argv[0]
translator = Translator()
subs= pysubs2.load(sys.argv[1], encoding="utf-8")
l=len(subs)
for i,line in enumerate(subs) :
	if line.text.find("{") == -1   :
		if line.text.find(r"\N")== -1 :
		    line.text = translator.translate(line.text,dest='ar').text
		else:
			pos= line.text.find(r"\N")
			line.text = translator.translate(line.text[:pos-1],dest='ar').text + r"\N"+ translator.translate(line.text[pos+1:],dest='ar').text
	else :
	    pos = line.text.find("}")
	    line.text = translator.translate(line.text[pos+1:],dest='ar').text
	printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'subbed', length = 50)

subs.save(sys.argv[2])


