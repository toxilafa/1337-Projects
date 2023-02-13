#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

#define _GNU_SOURCE 

int			main(int argc, char **argv)
{
	char *params[2];
	int num;
	
	num = atoi(argv[1]);
	if (num != 423)
		fwrite("NO !\n", 1, 5, stderr);
	else
	{
		params[0] = strdup("/bin/sh");
		params[1] = 0;
		setresgid(getegid(), getegid(), getegid());
		setresuid(geteuid(), geteuid(), geteuid());
		execv("/bin/sh", params);
	}
	return (0);
}	
