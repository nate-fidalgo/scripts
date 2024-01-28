
'''

    ____        __  __                   ____             _ ____   
   / __ \__  __/ /_/ /_  ____  ____     / __ )_________ _(_) / /__ 
  / /_/ / / / / __/ __ \/ __ \/ __ \   / __  / ___/ __ `/ / / / _ \
 / ____/ /_/ / /_/ / / / /_/ / / / /  / /_/ / /  / /_/ / / / /  __/
/_/    \__, /\__/_/ /_/\____/_/ /_/  /_____/_/   \__,_/_/_/_/\___/ 
      /____/                                                       


Unified English Braille (UEB) is based on Standard English Braille (SEB), with some significant changes.
These changes are designed to take away ambiguity and provide a braille code for the entire English-speaking world

neat short application allows one to convert a english book to a brallie book or visa-versa.

Note this is brallie for english language there are other braille dialects out for other countries.
I only support english dilect currently

As well i only currently supporting letters and numbers not punctuations/special characters.
Perhaps latter i will add to this to support any englished based books with non-scientific/math symbols.

Pretty neat stuff

'''

numstart = '⠼' #usually used to indicate the start of a number sequence to differentiate it from a-j letters (currently not supported)
numend ='⠰' # used to indicate a transition from numbers to letters as well as other things (currently not supported)
numlist = ['⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚']
numsyms = ['1','2','3','4','5','6','7','8','9','0']

strcapletterindicator = '⠠' #used to distingush lower case letters from upper case (currently not supported)
letterlist = ['⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']
lettersyms = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def getBrallieLetterIndex( b_letter ):	
	i=0
	while i < len(letterlist):
		if b_letter == letterlist[i]:
			return i ;
		i+=1
	return -1 ;

def getLetterIndex( letter ):
	i = 0
	while i < len(lettersyms):
		if letter == lettersyms[i]:
			return i ;
		i+=1	
	return -1 ;


def getLetterSymbol( index ):
	if index < len(lettersyms) and index >= 0 :	
		return lettersyms[index] ;
	return -1 ;

def getBrailleLetterSymbol( b_letter_index ):
	if b_letter_index < len(letterlist) and b_letter_index >= 0 :
		return letterlist[b_letter_index]
	return -1 ;

def getNumberSymbol( index ):
	if index < len(numsyms) and index >= 0 :
		return numsyms[index]	
	return -1 ;

def getBrallieNumberSymbol( index ):
	if index < len(numlist) and index >= 0 :
		return numlist[index]	
	return -1 ;		


#Testing the english to brallie conversion
expression = input("Enter a expression to convert to brallie: ")

for letter in expression:
	lindex = getLetterIndex( letter )
	bsym = getBrailleLetterSymbol(lindex)
	print(bsym + " ", end="") 


print() ;

#Testing the braille to english conversion
bexpression = input("Enter the braille symbols to convert to english: ")

for letter in bexpression:
	lindex = getBrallieLetterIndex( letter )
	bsym = getLetterSymbol(lindex)
	if bsym != -1 :			
		print(bsym + " ", end="") 

print() ;

