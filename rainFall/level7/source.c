#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char *p;

int m(void)
{
	int t = time(0);
    return printf("%s - %d\n", p, t);
}

int main(int argc, char ** argv)
{
	FILE *f;
    char *s;
    char *d;
    
	s = malloc(8);
	d = malloc(8);
    strcpy(s, argv[1]);
    strcpy(d, argv[2]);
    
    f = fopen("/home/user/level8/.pass", "r");
    fgets(p, 68, f);
    puts("~~");
    return 0;
}
