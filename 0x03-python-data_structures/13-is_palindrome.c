#include "lists.h"

/**
  *list_len - A function that counts the elements of a list_t list
  *@h: A singly linked list
  *Return: The number of elements in the list.
  */

int list_len(listint_t *h)
{
	if (!h)
		return (0);
	return (1 + ((h->next) ? list_len(h->next) : 0));
}

/**
 * has_corres - Check if node data is palindromic
 * @node: Node to be checked
 * @idx: Index of node in list
 * @len: List Length
 * @head: Pointer to list
 * Return: 1 if palindromic else 0
 */

int has_corres(listint_t *node, int idx, int len, listint_t *head)
{
	int i = 0;
	int corr_i = (len - idx - 1);

	while (head)
	{
		if (i == corr_i)
			return (node->n == head->n);
		i++;
		head = head->next;
	}
	return (0);
}

/**
 * is_palindrome - Function to check if linked list is a palindrome
 * @head: Pointer that points to linked list head
 * Return: 0 if not palindrome else 1
 */

int is_palindrome(listint_t **head)
{
	int len_list, i = 0, range;
	listint_t *head_dup;

	if (!head)
		exit(98);

	len_list = list_len(*head);
	if (len_list == 0)
		return (1);

	head_dup = *head;
	range = len_list / 2;
	for (i = 0; i < range; i++)
	{
		if (!has_corres(head_dup, i, len_list, *head))
			return (0);
		head_dup = head_dup->next;
	}

	return (1);
}
