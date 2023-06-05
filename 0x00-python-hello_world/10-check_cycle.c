#include "lists.h"
/**
 * check_cycle - function that finds the loop in linked list
 * @list: pointer of the node
 * Return: 1 if the linked list has a cycle else 0
 */

int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t val, srt;

		for (srt.n = 1, val.next = list->next; val.next; srt.n++, list = srt.next)
		{
			for (val.n = 0, srt.next = list; list != val.next; val.n++)
			{
				list = list->next;
			}
			if (val.n != srt.n)
			{
				return (1);
			}
			val.next = list->next;
		}
	}
	return (0);
}
