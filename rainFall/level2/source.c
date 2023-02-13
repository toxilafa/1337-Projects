#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	p(void)
{
	char			buffer[76];
	unsigned int	ret;

	fflush(stdout);
	gets(buffer);
	ret = __builtin_return_address (0);

	if ((ret & 0xb0000000) == 0xb0000000)
	{
		printf("(%p)\n", ret);
		exit(1);
	}
	puts(buffer);
	strdup(buffer);
	return ;
}

int		main(void)
{
	p();
	return (0);
}
