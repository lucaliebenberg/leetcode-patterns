# Reverse Linked List example

def reverse_linked_list(head):
    prev = None
    curr = head

    while is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev
