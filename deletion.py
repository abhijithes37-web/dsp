class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

  
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

   
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

   
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

  
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_begin()
            return

        temp = self.head
        for i in range(1, position):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next


    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")



dll = DoublyLinkedList()


dll.insert_begin(20)
dll.insert_begin(10)
dll.insert_end(40)
dll.insert_end(50)
dll.insert_position(30, 3)

print("After Insertions:")
dll.display() 


dll.delete_begin()
print("\nAfter deleting from beginning:")
dll.display()  

dll.delete_end()
print("\nAfter deleting from end:")
dll.display()  

dll.delete_position(2)
print("\nAfter deleting from position 2:")
dll.display() 