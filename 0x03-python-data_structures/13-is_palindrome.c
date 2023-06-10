#include "lists.h"

/**
  *list_len - A function that counts the elements of a list_t list
  *@h: A singly linked list
  *Return: The number of elements in the list.
  */

int list_len(listint_t *h)
{
	int len = 0;

	while (h)
	{
		len++;
		h = h->next;
	}

	return (len);
}

/**
 * is_palindrome - Function to check if linked list is a palindrome
 * @head: Pointer that points to linked list head
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	int len_list, hlf_len, i = 0, sum_check = 0;
	listint_t *head_dup;

	if (!head)
		exit(98);

	head_dup = *head;
	len_list = list_len(head_dup);
	if (len_list == 0)
		return (1);

	hlf_len = len_list / 2;
	while (head_dup)
	{

		if (i < hlf_len)
			sum_check += head_dup->n;
		else
		{
			if ((len_list % 2) && (i == hlf_len))
				;
			else
				sum_check -= head_dup->n;
		}
		i++;
		head_dup = head_dup->next;
	}

	return (sum_check == 0);
}
