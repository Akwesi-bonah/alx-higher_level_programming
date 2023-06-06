#include "lists.h"
/**
 * add_nodeint_begin - Adds a new node at the beginning of a list.
 * @head: where to add the node.
 * @n: int to add.
 * Return: the adress of new head node.
 */
listint_t *add_nodeint_begin(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (*head);
}
/**
 * insert_node - function that adds a new node in order on a list.
 * @head: where to list begin.
 * @number: int to insert.
 * Return: the adress of new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p, *before, *after;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	p = *head;
	new->n = number;
	if (p->n >= number)
	{
		new = add_nodeint_begin(head, number);
		return (new);
	}
	while (p->next != NULL)
	{
		if (p->n == number)
		{
			new->next = p->next;
			p->next = new;
			return (new);
		}
		before = p;
		after = before->next;
		if (before->n < number && after->n > number)
		{
			new->next = after;
			before->next = new;
			return (new);
		}
		p = p->next;
	}
	new = add_nodeint_end(head, number);
	return (new);
}
