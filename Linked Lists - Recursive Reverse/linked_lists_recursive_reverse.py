"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse(head):
    """
    Recursively reverses a singly linked list
    in place and returns the new head node.
    """
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
