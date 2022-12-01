#include <stdio.h>
#include <cs50.h>
#include <string.h>

//int string_length(string s);

int main(void){
    string name = get_string("Name: ");
    int length = strlen(name);
    printf("%i\n", length);
}

//int string_length(string s){
//    int i = 0;
//	while (s[i] != "\n"){
//		i++;
	//}
	//return i;
//}