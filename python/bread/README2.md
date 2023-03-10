A neat way to add different sections to a pe or elf binary. Is to use some gnu extension keywords.

<pre>
<code>
__attribute__((section("MYNEWSECTION")))
int k = 1000 ;
</code>
</pre>
<br>
That way when you do an objcump -h your.exe you will see a MYNEWSECTION in it with the contents of 1000
<br>
Below gives a read only data section as oppose to a read/write data section as above.

<pre>
<code>
__attribute__((section("MYNEWREADONLYSECTION")))
const int k = 1000 ;
</code>
</pre>
<br>
Note the const key word this tells the linker to make it a read only data section similar to built-in .rodata section.
<br>

Using these few gnu extension keywords one can define a preprocessor directive such as this to act like a typedef but at the preprocessing stages.
So you dont have to type that long string every time you want a piece of data to go into a specific section/segment in a elf or pe binary.
<br>

<pre>
<code>
#define MYRODATASECTION  __attribute__((section("RODATASEC"))) const
#define MYDATASECTION    __attribute__((section("DATASEC"))) 
int k = 1000 ;
int m = 59 ;
MYRODATASECTION int j = 20 ;  // goes into RODATASEC which is read only data section
MYDATASECTION int g = 20 ;    // goes into DATASEC   which is read/write data section
...
</code>
</pre>
<br>
Used in conjunction with butter.py you can now not only embed images,videos,exe, files ,...etc into a binary but also tell it what section or define your own section to put them in by using the gnu extensions and a few preprocessor directives.

