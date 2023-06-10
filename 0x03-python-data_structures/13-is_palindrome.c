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
 * node_data_arr - Function to create array of a linked list data
 * @head: Pointer to head of linked list
 * @len: Size of Array.
 * Return: Pointer to created array
 */

int *node_data_arr(listint_t *head, int len)
{
	int *arr_of_data = NULL, i = 0;

	arr_of_data = malloc(sizeof(int) * len);
	if (!arr_of_data)
		return (NULL);

	while (head)
	{
		arr_of_data[i++] = head->n;
		head = head->next;
	}
	return (arr_of_data);
}

/**
 * is_palindrome - Function to check if linked list is a palindrome
 * @head: Pointer that points to linked list head
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	int len_list, i = 0, *arr_of_d = NULL;
	listint_t *head_dup;

	if (!head)
		exit(98);

	head_dup = *head;
	len_list = list_len(head_dup);
	if (len_list == 0)
		return (1);

	arr_of_d = node_data_arr(head_dup, len_list);
	if (!arr_of_d)
		exit(98);

	for (i = 0; i < (len_list / 2); i++)
	{
		if (!(head_dup->n == arr_of_d[len_list - 1 - i]))
			return (0);
		head_dup = head_dup->next;
	}
	free(arr_of_d);
	return (1);
}
