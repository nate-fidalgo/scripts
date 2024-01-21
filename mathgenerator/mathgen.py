#!/usr/bin/python

'''
MMMMMMMM               MMMMMMMM               AAA         TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH      GGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNN
M:::::::M             M:::::::M              A:::A        T:::::::::::::::::::::TH:::::::H     H:::::::H   GGG::::::::::::GE::::::::::::::::::::EN:::::::N       N::::::N
M::::::::M           M::::::::M             A:::::A       T:::::::::::::::::::::TH:::::::H     H:::::::H GG:::::::::::::::GE::::::::::::::::::::EN::::::::N      N::::::N
M:::::::::M         M:::::::::M            A:::::::A      T:::::TT:::::::TT:::::THH::::::H     H::::::HHG:::::GGGGGGGG::::GEE::::::EEEEEEEEE::::EN:::::::::N     N::::::N
M::::::::::M       M::::::::::M           A:::::::::A     TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H G:::::G       GGGGGG  E:::::E       EEEEEEN::::::::::N    N::::::N
M:::::::::::M     M:::::::::::M          A:::::A:::::A            T:::::T          H:::::H     H:::::HG:::::G                E:::::E             N:::::::::::N   N::::::N
M:::::::M::::M   M::::M:::::::M         A:::::A A:::::A           T:::::T          H::::::HHHHH::::::HG:::::G                E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N
M::::::M M::::M M::::M M::::::M        A:::::A   A:::::A          T:::::T          H:::::::::::::::::HG:::::G    GGGGGGGGGG  E:::::::::::::::E   N::::::N N::::N N::::::N
M::::::M  M::::M::::M  M::::::M       A:::::A     A:::::A         T:::::T          H:::::::::::::::::HG:::::G    G::::::::G  E:::::::::::::::E   N::::::N  N::::N:::::::N
M::::::M   M:::::::M   M::::::M      A:::::AAAAAAAAA:::::A        T:::::T          H::::::HHHHH::::::HG:::::G    GGGGG::::G  E::::::EEEEEEEEEE   N::::::N   N:::::::::::N
M::::::M    M:::::M    M::::::M     A:::::::::::::::::::::A       T:::::T          H:::::H     H:::::HG:::::G        G::::G  E:::::E             N::::::N    N::::::::::N
M::::::M     MMMMM     M::::::M    A:::::AAAAAAAAAAAAA:::::A      T:::::T          H:::::H     H:::::H G:::::G       G::::G  E:::::E       EEEEEEN::::::N     N:::::::::N
M::::::M               M::::::M   A:::::A             A:::::A   TT:::::::TT      HH::::::H     H::::::HHG:::::GGGGGGGG::::GEE::::::EEEEEEEE:::::EN::::::N      N::::::::N
M::::::M               M::::::M  A:::::A               A:::::A  T:::::::::T      H:::::::H     H:::::::H GG:::::::::::::::GE::::::::::::::::::::EN::::::N       N:::::::N
M::::::M               M::::::M A:::::A                 A:::::A T:::::::::T      H:::::::H     H:::::::H   GGG::::::GGG:::GE::::::::::::::::::::EN::::::N        N::::::N
MMMMMMMM               MMMMMMMMAAAAAAA                   AAAAAAATTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH      GGGGGG   GGGGEEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNN
                                                                                                                                                                         
                                                                                                                                                                         
                                                                                                                                                                         
I nice program to generate math typeset svg images for embedding in webpages

How to use is create a file of all your math expressions in latex format each line in the file delimits a new expression
Important to remember each line is a new expression for a new svg image.

For example say i had a file named batchmathfile containing
-----------
$2+4$
$3^8$
\begin{equation}1 = \cos^2 \theta + \sin^2 \theta\end{equation}
$$6 = \cos^3 \theta + \sin^3 \theta$$
-----------

That means there are 4 distinct expressions that will create 4 distinct svg images
Each line delimits a new expression do not span multiple lines for your math expressions Very important or you will hang /have an error.

Usually if you hang on some output it means you have an error in your expression
To locate the error look at the output on your terminal to see what img tag its up to that will hint you to the line number in the file.

'''



import subprocess

CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'
LATEXFILENAME = 'LATEXGEN' #internal name used for generating dvi files for svg image generation


#Function used to check if you have the proper programs installed to use this library/program.
#Basically if you have "latex" and "dvisvgm" programs installed your all set
#If not usually they come with texlive packages if you are on linux/unix systems
def checkCapabilities(): 
	try:
		subprocess.call(["latex", "--version"],stdout = subprocess.DEVNULL)
	except:
		print(CRED+"Make sure you install latex command for processing tex files" + CEND+"\n" )
		print(CRED+"Usually the package name is texlive make sure its in your path"+ CEND)	
		exit(-1) ;
	try:
		subprocess.call(["dvisvgm", "--version"],stdout = subprocess.DEVNULL)
	except:
		print(CRED+"Make sure you install dvisvgm command for processing dvi files to svg"+ CEND)
		print(CRED+"Usually the package name is texlive make sure its in your path"+ CEND)
		exit(-1) ;

#Function that takes in a string that is the latex math expression and generates the tex file for processing
#Internal default name is held in LATEXFILENAME above! One can modify and use a different name if he wishes but not recommended 
#If one chooses to just remember the name has to be unique to the folder you are in when using this program/library
#or you might delete the file you had with that name.
def createLatexFile(mathexpression):
	f = open(LATEXFILENAME+".tex", "w")
	f.write("\\documentclass[14px,aspectratio=169]{article}\n")
	f.write("\\usepackage{amsmath}\n")
	f.write("\\usepackage{amssymb}\n")
	f.write("\\usepackage{amsfonts}\n")
	f.write("\\thispagestyle{empty}\n")
	f.write("\\begin{document}\n")

	f.write("%Your Latex Expression\n")
	f.write(mathexpression)

	f.write("\n\\end{document}")
	f.close()

#function to make the image given the output name you want to use for it (aka SVGOUTNAME)
def makeSVGIMG(SVGOUTNAME):
	result1 = subprocess.Popen(["latex" , LATEXFILENAME+".tex"],  stdout = subprocess.DEVNULL, universal_newlines=True)
	result1.wait() ;

	result2 = subprocess.Popen(["dvisvgm" , LATEXFILENAME+".dvi", "-o " + SVGOUTNAME +".svg" ], stderr=subprocess.DEVNULL, stdout = subprocess.DEVNULL, universal_newlines=True)
	result2.wait() ;

#function to print a nice string to the console so one can easily embedded this svg image in a webpage
def printIMG(SVGOUTNAME,MSTR,PREPENDPATH="",WIDTH="50",HEIGHT="20"):
	print(CGREEN+"<img src=\""+ PREPENDPATH + SVGOUTNAME+".svg\" " + "style=\"vertical-align: middle\"" + " alt=\""+ MSTR+ "\" width=\"" + WIDTH + "\" height=\""+ HEIGHT+"\">"+CEND) ;

#function to allow one to process multiple math expressions all at once
#filename: is a string name of the textfile where all the math statements are to process
#in this file one line corrosponds to a single math expression to process.
#Beware lines delimitate new expressions and the order the expressions are process is first line to last line in file.
#prependpath: is string to append to the beginning of the file name such as a dirpath/ 
#svgoutname: is string that is the basename of the svg outputs each output svg file is basename+1,2,3,...lastfileline
#width: is string representing the number value for the width of the img tag
#height is string representing the number value for the height of the img tag
def processMathFile(FILENAME,SVGOUTNAME,PREPENDPATH,WIDTH,HEIGHT):
	try:
		f = open(FILENAME, "r")
	except:
		print("Missing math processing file => " + FILENAME)
		exit(-1)
	mexprs=f.readlines() ;
	i=0	
	while   i < len(mexprs) :
		createLatexFile(mexprs[i].rstrip());
		makeSVGIMG(SVGOUTNAME+str(i)) ;
		printIMG(SVGOUTNAME+str(i),mexprs[i].rstrip(),PREPENDPATH,WIDTH,HEIGHT);
		i+=1 
	f.close() 

#FUNCTION TO CALL IF YOUR ONLY WANTING TO PROCESS ONE STATEMENT
#LATEX_MATHEXPRESSION: str representing math latex expression to process
#PREPENDPATH: str append a dirpath/ for the img tag or '' for appending nothing
#SVGOUTNAME: str name of svg outputfile
#WIDTH: str size of width for img tag
#HEIGHT: str size of height for img tag
def makeMathImage(LATEX_MATHEXPRESSION,SVGOUTNAME="MATHOUT",PREPENDPATH="",WIDTH="50",HEIGHT="20"):
	checkCapabilities() ;
	createLatexFile(LATEX_MATHEXPRESSION);
	makeSVGIMG(SVGOUTNAME) ;
	printIMG(SVGOUTNAME,LATEX_MATHEXPRESSION,PREPENDPATH,WIDTH,HEIGHT);

#FUNCTION TO CALL IF YOUR WANTING TO PROCESS MULTIPLE STATEMENT HELD IN MATH_BATCHFILE
#MATH_BATCHFILE: str name of the file containing all the math expressions to process one expression per line
#PREPENDPATH,SVGOUTNAME,WIDTH,HEIGHT: these parameters are the same as makeMathImage function
def makeMathImages(MATH_BATCHFILE,SVGOUTNAME,PREPENDPATH="",WIDTH="50",HEIGHT="20"):
	checkCapabilities() ;
	processMathFile(MATH_BATCHFILE,SVGOUTNAME,PREPENDPATH,WIDTH,HEIGHT) ;



mfile=input("Enter the latex math processing filename:\n")
pfile=input("Enter name to generate images with:\n(example name=MATH creates MATH1.svg,MATH2.svg,...)\n")
prep=input("Enter a name to prepend for img tags or hit enter for nothing:\n(example if name=dirpath then <img src=dirpath/Math1.svg...>\ninstead of just <img src=Math1.svg...>) if left blank\n ")
width=input("Enter a number for size of width of img tag or hit enter for (default=50):\n")
height=input("Enter a number for size of height of img tag or hit enter for (default=20):\n")

if( prep.strip(' \t\n\r') == "" ):
	prep="" ;

if( width.strip(' \t\n\r') == "" ):
	width = "50" ;

if( height.strip(' \t\n\r') == ""):
	height = "20" ;

makeMathImages(mfile,pfile,prep,width,height) ;
print("Goodbye :) !!!") ;

