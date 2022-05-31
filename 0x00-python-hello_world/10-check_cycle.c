#include "lists.h"

/**
 * check_cycle - checks if singly linkec list has cycle in it
 * @list: singly linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slowptr = list;
	listint_t *fastptr = list;

	while (slowptr && fastptr && fastptr->next)
	{
		slowptr = slowptr->next;
		fastptr = fastptr->next->next;

		if (fastptr == slowptr)
		{
			return (1);
		}
	}

	if (!list)
	{
		return (0);
	}
}
