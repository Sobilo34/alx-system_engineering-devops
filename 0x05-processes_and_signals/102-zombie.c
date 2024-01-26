#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int infinite_while(void);

/**
 * main - A C program that creates 5 zombie processes
 * Return: It returns 0
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - A function for infinite while loop
 * @void: The function has no parameter
 * Return: It returns 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
