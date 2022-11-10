#include <cs50.h>
#include <stdio.h>

int main(void)
{
	// comment 
	int x = get_int("x: ");
	int y = get_int("y: ");

	float z = (float) x / (float) y; // (float) x converts x from int to float

	printf("%.2f\n", z);
}
