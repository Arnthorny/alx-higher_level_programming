#include "lists.h"
/**
  *check_cycle - check if linked list has a cycle.
  *@list: A singly linked list
  *Return: 0 if there's no cycle else return 1.
 */

int check_cycle(listint_t *list)
{
	const listint_t *s = list, *f = list;
	short int firstMatch = 0;

	if (!list)
		exit(98);

	while (s)
	{
		s = s->next;
		if (!firstMatch)
			f = f ? (f->next ? f->next->next : NULL) : NULL;
		else
			f = f ? f->next : NULL;

		if (f && f == s)
		{
			if (firstMatch)
				return (1);
			s = list;
			firstMatch = 1;
		}

	}
	return (0);
}

