#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Runs an infinite loop to keep the parent process alive.
 * Return: Always 0.
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
 * main - Creates 5 zombie processes.
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == -1)
		{
			perror("fork failed");
			return (1);
		}
		if (pid == 0)
		{
			/* Child process immediately exits to become a zombie */
			exit(0);
		}
		else
		{
			/* Parent process prints the PID of the zombie */
			printf("Zombie process created, PID: %d\n", pid);
		}
	}

	/* Keep the parent process alive to maintain zombie state of children */
	infinite_while();

	return (0);
}
