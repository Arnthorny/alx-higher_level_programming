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
	int len_list, i = 0, *arr_of_d;

	if (!head)
		exit(98);

	len_list = list_len(*head);
	if (len_list == 0)
		return (1);

	arr_of_d = node_data_arr(*head, len_list);
	if (!arr_of_d)
		exit(98);
	
	for (i = 0; i < (len_list / 2); i++)
	{
		if (!((*head)->n == arr_of_d[len_list - 1 - i]))
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
