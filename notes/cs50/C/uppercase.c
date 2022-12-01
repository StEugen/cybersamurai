#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void){
    string s = get_string("Bef: ");
    printf("after");
    for (int i = 0 , n = strlen(s); i < n; i ++){
        if (s[i] >= 'a' && s[i] <= 'z'){
            printf("%c", s[i] = 32);
        }
        else{ 
            printf("%c", s[i]);
        }
    }
}