#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
int main()
{
	char *command;
	strcpy(command, "python3 server.py");
	system(command);
	return 0;
}
