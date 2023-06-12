#include "lists.h"
/**
 * is_palindrome - checks id a singly  linked list is a palindrome
 * @head: linked list
 *
 * Return: 1 is true else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	int i = 0, j = 0;
	int size = 0, flag = 1;
	int *a = NULL;

	if (head == NULL || *head == NULL)
	{
		return (flag);
	}

	ptr = *head;
	while (ptr->next != NULL)
	{
		size++;
		ptr = ptr->next;
	}

	a = malloc(sizeof(int) * size + 1);
	ptr = *head;
	
	while (ptr != NULL)
	{
		a[i] = ptr->n;
		i++;
		ptr = ptr->next;
	}
	j = size;
	for (i = 0; i <= size / 2; i++, j--)
	{
		if (a[i] != a[j])
		{
			flag = 0;
		}
	}

	free(a);
	return (flag);
}
