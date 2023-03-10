I neat way to add different sections to a pe or elf binary. Is to use some gnu extension keywords.

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
