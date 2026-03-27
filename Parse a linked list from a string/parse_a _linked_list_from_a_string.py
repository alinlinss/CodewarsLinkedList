"""Functon Node"""
class Node():
    """A node in a singly linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Converts a string formatted as '1 -> 2 -> None' into a linked list.
    Returns the head Node of the created list, or None if empty.
    """
    parts = list_repr.split(" -> ")

    if parts[0] == "None":
        return None

    head = Node(int(parts[0]))
    current = head

    for part in parts[1:]:
        if part == "None":
            break
        current.next = Node(int(part))
        current = current.next

    return head
