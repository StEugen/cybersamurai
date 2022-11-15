#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int points = get_int("Hom many pointd did you lose? ");
    const int MINE = 2;

    if (points < MINE)
    {
        printf("You lost fewer\n");
    }
    else if (points > MINE)
    {
        printf("You lost more points\n");
    }
    else 
    {
        printf("Same");
    }
}