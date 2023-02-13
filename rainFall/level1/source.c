#include <stdio.h>
#include <stdlib.h>

int		run(void)
{
	fwrite("Good... Wait what?\n", 19, 1, stdout);
	return (system("/bin/sh"));
}

int		main(void)
{
	char	buffer[76];

	gets(buffer);
	return (0);
}
