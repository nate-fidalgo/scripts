This is a simple programming script to allow one to embed nearly any file into a binary and access it easily. <br>
Example of how it works follows<br>

<pre>
<code>
python bread.py -h 
</code>
</pre>
<br>
Gives
<br>
<pre>
<code>
bread.py -i <inputfile> -o <outputfile> -m <mode>
mode options:= both | short | long
</code>
</pre>
<br>
Assuming you have an executable named example.exe that you want to embed in a c/c++ header file out.h
<br>
<pre>
<code>
bread.py -i example.exe -o out.h -m both
</code>
</pre>
<br>
Gives output to screen as 
<br>
<pre>
<code>
bread.py gave butter!!! 
Input file is  example.exe
Output file is  out.h
</code>
</pre>
