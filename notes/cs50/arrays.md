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

<h2>Debugging</h2>
Print is the most common tool for debugging, so you can see what happening in computer memory <br>
Debuggers let you to go step by step <br>
rubber duck debugging - is an idea of talking to something about what's going on in your code. Talking through your code step by step can help to debug. <br>

<h2>Memory</h2>
bool 1 byte <br>
char 1 byte<br >
double 8 bytes <br>
float 4 bytes <br>
int 4 bytes <br>
long 8 bytes <br>
string ? bytes <br>
RAM - random access memory, the place where memory is<br>
<pre>
    int score3 = 33;
    
    printf("Average %f\n", (score1 + score2 +score3) / 3);
}
</pre>
so, here we have three ints devided by int but C treats it like float, so the error. 
<br>
<pre>
    printf("Average %f\n", (score1 + score2 +score3) / 3.0);
}
</pre>
So, if we make one value as float (3.0) we won't have errors <br>

<h2>Array</h2>
Array is type of data that allows us to store multiple values of the same type back-to-back <br>
<pre>
int scores[3];
</pre>
This array will store 3 integers. <br>
scores[0] = 72; <br>
scores[1] = 73; <br>
scores[2] = 33; <br>



