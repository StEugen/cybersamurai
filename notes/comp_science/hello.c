#include <stdio.h>
#include <cs50.h>

int main(void)
{
	string answer = get_string("What's ur name? ");
	printf("Hello, %s\n", answer);
}
