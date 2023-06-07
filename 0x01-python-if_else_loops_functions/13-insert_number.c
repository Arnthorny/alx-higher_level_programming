#include "lists.h"

/**
 *  det_node_i - Function to determine index, node be inserted
 *  @head: Head of linked list
 *  @number:Number to be inserted
 *  Return: Index or -1 if failed
 */
int det_node_i(listint_t **head, int number)
{
	listint_t *curr;
	int i = 0;

	if (head == NULL)
		return (-1);
	else if (*head == NULL)
		return (0);
	curr = *head;
	while (curr)
	{
		if (curr->n <= number)
			curr = curr->next;
		else
			return (i);
		i++;
	}
	return (i);
}



/**
 *  insert_node - A function that inserts a number in a sorted list
 *  @head: Head of linked list
 *  @number:Number to be inserted
 *  Return: Address of new node or NULL if failed
 *
 */


listint_t *insert_node(listint_t **head, int number)
{
	int loca = det_node_i(head, number), i = 0;
	listint_t *new, *curr;

	if (loca == -1)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	curr = *head;
	new->n = number;
	new->next = NULL;

	while (curr)
	{
		if (i == loca && curr == *head)
		{
			new->next = curr;
			*head = new;
			return (new);
		}
		else if (i == loca - 1)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}

		curr = curr->next;
		i++;
	}
	return (NULL);
}
