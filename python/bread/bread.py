"""
A Simple Python program to build a binary character array of a file which can then be included into a c/c++ program
OR Embedded into a ELF or PE binary.

The file to which the binary character array is created from can be nearly anything from a jpeg,png, resource file , audio file, or even another executable file.
Great for embedding files with in an executable that normally thought couldnt be easily done and have the embeddings easily accessible to use in your program.

There are two forms of embedding long form or short form you can toggle between them with -m short or -m long 
If you want both embeddings you can use -m both these are command line switches for bread.py

For more info on how to use the program type:   python bread.py -h 

Written by Nate
Questions , comments, bugs , improvements can be send to the email below
No promises are made to respond in a timely fashion or even at all but all do my best to clear any issues.

"""
import sys, getopt
orig_stdout = sys.stdout
COLNUMBERS = 10 ; #for readability change to desired number of columns you want default is 10


def longForm(FILE , COLNUMBERS):
 with open(FILE, "rb") as f:
    byte = f.read(1)
    bcode = [] ;
    print( "unsigned char butter1[] = {" ) ; 
    while byte != b"":
        bcode.append( byte.hex() )
        byte = f.read(1)
    for i in range(0, len(bcode) - 1  ) :
            print( r"0x" +  bcode[i]  +"," ,  end ="") ;
            if i % COLNUMBERS == 0 and i != 0 :
               print() ; 
    print( r"0x" +  bcode[len(bcode)-1]    ,  end ="") ;
    print( "} ;" ) ; 
 return ;
    
    
def shortForm(FILE, COLNUMBERS):
 with open(FILE, "rb") as f:
       byte = f.read(1);
       bcode = [] ;
       while byte != b"":
        bcode.append( byte.hex() )
        byte = f.read(1)
       print( r'unsigned char butter2[] = "'  ,  end ="") ;
       for i in range(0, len(bcode) - 1  ) :
        if i % COLNUMBERS == 0 and i != 0 :
            print(chr(92)) ;
        print( r"\x" +  bcode[i]   ,  end ="") ;
       print( r'" ;' ) ;
      
 return ;


def main(proname , argv):
   inputfile = ''
   outputfile = ''
   mmode = ''
   opts, args = getopt.getopt(argv,"hm:i:o:",[ "mode=" , "ifile=","ofile="])
   for opt, arg in opts:
      if opt == '-h':
         print ( proname[0] + ' -i <inputfile> -o <outputfile> -m <mode>')
         print ( 'mode options:= both | short | long')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-m" ,  "--mode") :
          mmode = arg 
   if inputfile == '' :
       print(proname[0] + " -i <NO INPUT FILE ERROR>!!! ") ;
       sys.exit() ;
        
   print(proname[0] + " gave butter!!! ") ;
   print ('Input file is ', inputfile)
   if outputfile == '' :
    print("Output file is butter.h") ;  
   else :
    print ('Output file is ', outputfile) ;
   if inputfile == '' :
       print ( proname[0] + ' -i <NO INPUT FILE ERROR> -o <outputfile>')
       sys.exit()
   if outputfile == '' :
       f = open("butter.h", "w")
       sys.stdout = f ;
       dumpdata( inputfile ,  mmode )
   elif outputfile !=  '' :
       f = open(outputfile, "w")
       sys.stdout = f ;
       dumpdata( inputfile ,  mmode )
       

def dumpdata( inputfile ,  mode ):
       if mode == 'both' :
           longForm(inputfile , COLNUMBERS) ;
           print() ;
           shortForm(inputfile, COLNUMBERS) ;
       elif mode == 'short' :
          shortForm(inputfile, COLNUMBERS) ;
       elif mode == 'long' :
        longForm(inputfile , COLNUMBERS) ;
       else :
          longForm(inputfile , COLNUMBERS) ;
          print() ;
          shortForm(inputfile, COLNUMBERS) ;    

if __name__ == "__main__":
   main(sys.argv[0:1] ,  sys.argv[1:])

