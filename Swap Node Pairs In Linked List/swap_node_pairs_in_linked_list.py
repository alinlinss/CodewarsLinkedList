"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    """Swaps each pair of adjacent nodes in the list and returns the new head."""
    placeholder = Node(next=head)
    before_pair = placeholder

    while before_pair.next and before_pair.next.next:
        first = before_pair.next
        second = before_pair.next.next

        before_pair.next = second
        first.next = second.next
        second.next = first

        before_pair = first

    return placeholder.next
