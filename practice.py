class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head == None:
            print("This Linked List is empty.")
            return

        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


n1 = Node(7)
n2 = Node(13)
n3 = Node(22)

l_list = LinkedList()
l_list.add_to_start(n3)
l_list.add_to_start(n2)
l_list.add_to_start(n1)
l_list.print_linked_list()
        