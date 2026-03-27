class Node(object):
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """Stores the updated source and destination linked lists."""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Moves the first node from source to destination and returns updated lists in Context."""
    if source is None:
        raise Exception("Source list is empty")

    new_source = source.next
    source.next = dest
    new_dest = source

    return Context(new_source, new_dest)
