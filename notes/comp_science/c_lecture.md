<h1>C lecture</h1>
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




