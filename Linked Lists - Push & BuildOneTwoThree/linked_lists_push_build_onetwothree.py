"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    """Insert a new node at the beginning of the list.

    Args:
        head: Current head of the list
        data: Value to insert

    Returns:
        New head of the list
    """
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """Create a linked list with values 1 -> 2 -> 3.

    Returns:
        Head of the linked list
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
