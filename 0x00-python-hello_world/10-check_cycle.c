#include "lists.h"
/**
  *check_cycle - check if linked list has a cycle.
  *@list: A singly linked list
  *Return: 0 if there's no cycle else return 1.
 */

int check_cycle(listint_t *list)
{
	const listint_t *s = list, *f = list;

	while (s)
	{
		s = s->next;
		f = f ? (f->next ? f->next->next : NULL) : NULL;
		
		if (f && s && f == s)
			return (1);

	}
	return (0);
}

