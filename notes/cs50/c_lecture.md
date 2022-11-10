<h1>C lecture</h1>
<code>clang test.c -o test -lcs50</code> <br>
Correctness: Is code correct? <br> 
Design: Is code well designed? <br>
Style: Is code pretty written? <br>
<pre>
#include <stdio.h>

int main(void)
{
	printf("hello, world\n");
}
</pre>
<br>
IDE - Integrated Development Environment - actually code editor.<br>
source code -> compiler -> machine code <br>
<h2>Functions</h2>
arguments -> function -> side effects <br>
functions can return values. <br>
string answer = get_string("What's your name? "); <br>
"=" is not an equality, it gives value from right value of left <br> 
string - words; int - integer - numbers; <br>
Capitalization matters <br>
<pre>
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string answer = get_string("What's your name? ");
        printf("hello, %s\n", answer);
}
</pre>
<br>
<pre>
sudo apt install libcs50
export CC="clang"
export CFLAGS="-fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow"
export LDLIBS="-lcrypt -lcs50 -lm"
source ~/.bashrc
sudo apt-get install clang 
make code_name
</pre>
<br>
<code> int main</code> is the place where programm starts <br>
Header files are files in the top of programm <code> #include <stdio.h> </code> <br>
<h2>Types</h2>
Bool <br>
char <br>
double <br>
float <br>
int <br>
long <br>
string <br> 
get_[variable-type] <br>
<h2>Format codes</h2>
%c - char <br>
%f - float <br>
%i - integer <br>
%li - long <br>
%s - string<br>
<h2>Operators</h2>
Same as in python <br>
<br>
counter = counter + 1; counter += 1; counter++; all the same <br>
<h2>Conditions</h2>
<pre>
if (x < y)
{
	printf("x is less than y\n");
}
</pre>
<br>
<pre>
if (condition)
{
	printf("");
}
else
{
	printf("");
}
</pre>
<br>
<pre>
if (condition)
{
	printf("");
}
else if (other condition)
{
	printf("");
}
else (other condition)
{
	printf("");
}
</pre>
<br> 
Constat - variable that cannot be changed. Constants are made with <code>const type variable</code>. Constants can be made UPCASE so better seen in code <code>const int MINE</code><br>
Single quotes '' for single character<br>
Double quotes "" for string <br>
<h2>Loops</h2>
<pre>
while (true)
{
	printf("");
}
</pre>
<br>
<pre>
int i = 0;
while (i < 3)
{
	printf("");
	i++;
}
</pre> 
<br>
<pre>
for (int i = 0; i < 3; i++)
{
	printf("");
}
</pre>
<br>
int i = 0; - initialization <br>
i < 3; - constant boolean expression check <br>
i++; - update <br>
Global declaration - int i = 0; <br>
Local declaration - for (int i....) <br>
<pre>
int n;
do
{
	n = get_int("Width: ");
}
while (n < 1);
</pre>
<h2>Functions</h2>
<pre>
void meow(void)
{
	printf("");
}
</pre>
first void means type of function <br>
meow means name of function <br>
(void) means if function takes any inputs <br>
C reads code from top to bottom <br>
If you want to leave your function after <code>int main(void)</code> function, you need to specify it at the top: <br>
<pre>
void meow(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        meow();
    }
    
    
}

void meow(void)
{
    printf("meow\n");
}
</pre>
<br>
floating point imprecision <br>
Truncation - when deviding int by int, and trying to store the result in something else, C will throw it <br>

  



