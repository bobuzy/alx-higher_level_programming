#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Check if the list is a cycle
 *
 * @list: The list to be checked
 * Return: 1, if it's a cycle. 0, otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *ptrr = list;

	while (ptrr && ptrr->next)
	{
		ptr = ptr->next;
		ptrr = ptrr->next->next;
		if (ptr == ptrr)
			return (1);
	}
	return (0);
}
