"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """Returns the node at the given index in a linked list or raises an exception if the index is invalid."""
    if index < 0:
        raise Exception("Index out of bounds")

    current = node
    for _ in range(index):
        if current is None:
            raise Exception("Index out of bounds")
        current = current.next
    if current is None:
        raise Exception("Index out of bounds")
    return current
