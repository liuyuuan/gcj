#include<stdio.h>
#include<string.h>

void translate(char c);

int main()
{
    char s[1001];
    fgets(s,1001,stdin);
    int i;
    for(i=0; i<strlen(s); i++)
      translate(s[i]);
    return 0;
}
