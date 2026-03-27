"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    """
    Inserts a new node with the given data into its correct
    position within a sorted linked list to maintain ascending order,
    and returns the updated head.
    """
    new_node = Node(data)

    if head is None or data <= head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head
