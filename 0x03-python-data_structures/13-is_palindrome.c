#include "lists.h"

/**
 * is_palindrome - check a given linked list is palindrome or not
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *fast = *head, *slow = *head, *half = NULL;

	if (head == NULL || (*head)->next == NULL || *head == NULL)
		return (0);
	while (fast)
	{
		fast = fast->next->next;
		if (!fast)
		{
			half = slow->next;
			break;
		}
		else if (!fast->next)
		{
			half = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	revrse_list(&half);

	while (tmp && half)
	{
		if (tmp->n == half->n)
		{
			tmp = tmp->next;
			half = half->next;
		}
		else
			return (0);
	}

	if (half == NULL)
		return (1);
	return (0);
}

/**
 * revrse_list - this fuction reverse a linked list
 * @head: the head of the liked list
 */
void revrse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
