#include <cs50.h>
#include <stdio.h>

int main(void)
{
	// comment 
	long x = get_int("x: ");
	long y = get_int("y: ");
	long z = x + y;
	printf("%i\n", z);
}
