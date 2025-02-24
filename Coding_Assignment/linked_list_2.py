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

    def merge_if_match(self, second_list):
        """Merges the second list into the first if the first element of the second list is found in the first list"""
        if not self.head or not second_list.head:
            return

        match_value = second_list.head.data  # First element of second list
        temp = self.head

        # Find the node where match occurs
        while temp:
            if temp.data == match_value:
                # Merge the second list at this node
                second_tail = second_list.head
                while second_tail.next:
                    second_tail = second_tail.next
                second_tail.next = temp.next
                temp.next = second_list.head
                return
            temp = temp.next

# Example usage
if __name__ == "__main__":
    # First linked list
    ll1 = LinkedList()
    ll1.add_node(10)
    ll1.add_node(20)
    ll1.add_node(30)
    ll1.add_node(40)

    print("First Linked List:")
    ll1.display_list()

    # Second linked list
    ll2 = LinkedList()
    ll2.add_node(20)  # Match occurs at 20
    ll2.add_node(25)
    ll2.add_node(35)

    print("\nSecond Linked List:")
    ll2.display_list()

    # Merge if match
    ll1.merge_if_match(ll2)

    print("\nMerged Linked List:")
    ll1.display_list()
