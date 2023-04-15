class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def reverse_linked_list(head):
    current = head
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# пример
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
new_head = reverse_linked_list(head)
current = new_head
while current is not None:
    print(current.value)
    current = current.next