"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context(object):
    """
    class Context
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Splits a linked list into two by taking alternating nodes into each sublist."""
    if head is None or head.next is None:
        raise Exception("List must have at least two nodes")

    first = head
    second = head.next

    current_first = first
    current_second = second

    while current_first.next and current_first.next.next:
        current_first.next = current_first.next.next
        current_first = current_first.next

        current_second.next = current_second.next.next if current_second.next else None
        current_second = current_second.next

    current_first.next = None
    if current_second:
        current_second.next = None

    return Context(first, second)
