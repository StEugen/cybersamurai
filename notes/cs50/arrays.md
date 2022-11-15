<h1>Arrays</h1>
<pre>
#include <stdio.h>
#include <cs50.h>

int main(void)
{
	string answer = get_string("What's ur name? ");
	printf("Hello, %s\n", answer);
}
</pre>
When you compile your code, you do:<br>
1) preprocessing means to find libraries, so code in computer looks like this:<br>
<pre>
...
string get_string(string prompt);
int printf(string format, ...);
...

int main(void)
{
	string answer = get_string("What's ur name? ");
	printf("Hello, %s\n", answer);
}
</pre>
2) compiling is a real compiling, so C code becomes assembly<br>
3) assembling means to turn assembly code to zeros and ones<br>
4) linking means to link all files (myfile.c, cs50.c and stdio.c) in one file <br>


