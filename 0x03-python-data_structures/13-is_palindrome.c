#include<stdio.h>
#include"lists.h"

/**
 * _strlen_recursion - function that returns the length of a string
 *
 * @head: string to receive
 *
 * Return: int
 */


int _strlen_recursion(listint_t **head)
{
	if (*(*head) == NULL)
		return (0);
	head++;
	return (1 + _strlen_recursion(head));
}

/**
 * get_pal - check if is 0 or 1
 * @head: input string
 * @len: length
 * Return: int
 */

int get_pal(listint_t **head, int len)
{
	if (*(*head) != *(*head) + (len - 1))
		return (0);
	else if (*(*head) == NULL)
		return (1);
	return (get_pal(head + 1, (len - 2)));
}

/**
 * is_palindrome - returns 1 if a string is a palindrome and 0 if not.
 * @head: input char
 *
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	int len;

	len = _strlen_recursion(head);
	if (len <= 1)
		return (1);
	return (get_pal(head, len));
}
