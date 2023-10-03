#include "lists.h"

/**
 * insert_node - nserts a number into a sorted singly linked list
 * @head: the head of the linked list
 * @number: the number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *tmp;

	if (head == NULL && *head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	tmp = *head;
	if (tmp->n > number)
		node->next = tmp;
	else
	{
		while (tmp != NULL)
		{
			if (tmp->next->n > number)
			{
				node->next = tmp->next;
				tmp->next = node;
				break;
			}
			else if (tmp->next == NULL)
				tmp->next = node;	
			tmp = tmp->next;
		}
	}
	return (node);
}

