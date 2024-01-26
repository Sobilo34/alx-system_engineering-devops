#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int infinite_while(void);

/**
 * main - This is a function that create 5 zombie processes
 * Return: return 0
 */
int main(void)
{
	int i;
	pid_t prs_id, wait_pid;

	for (i = 0; i < 5; i++)
	{
		prs_id = fork();
		if (prs_id == -1)
		{
			perror("fork");
			exit(1);
		}
		else if (prs_id == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			sleep(1);
			exit(0);
		}
		else
		{
			wait_pid = wait(NULL);
			if (wait_pid == -1)
			{
				perror("wait");
				exit(1);
			}
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
