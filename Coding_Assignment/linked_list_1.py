class Node:
    """A node of the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked list class"""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Deletes the first occurrence of a node with the given value"""
        temp = self.head

        # If the head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"Value {key} not found in list!")
            return

        prev.next = temp.next
        temp = None

    def display_list(self):
        """Displays the linked list"""
        temp = self.head
        if not temp:
            print("List is empty!")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def display_reverse_helper(self, node):
        """Helper function to print the list in reverse using recursion"""
        if not node:
            return
        self.display_reverse_helper(node.next)
        print(node.data, end=" -> ")

    def display_reverse(self):
        """Displays the linked list in reverse order"""
        print("Reversed List: ", end="")
        self.display_reverse_helper(self.head)
        print("None")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    ll.display_list()        # Output: 10 -> 20 -> 30 -> 40 -> None
    ll.display_reverse()     # Output: 40 -> 30 -> 20 -> 10 -> None

    ll.delete_node(20)
    ll.display_list()        # Output: 10 -> 30 -> 40 -> None
    ll.display_reverse()     # Output: 40 -> 30 -> 10 -> None
