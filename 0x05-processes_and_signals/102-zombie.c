#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Description: This function creates an infinite loop that
 * keeps the parent process running
 *
 * Return: Always 0 (though it never actually returns)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes
 *
 * Description: This program creates 5 zombie processes by forking
 * child processes that immediately exit while the parent continues
 * to run
 *
 * Return: 0 on success, 1 on failure
 */
int main(void)
{
	pid_t child_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid < 0)
		{
			perror("Error:");
			return (1);
		}
		if (child_pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}

	infinite_while();

	return (0);
}
