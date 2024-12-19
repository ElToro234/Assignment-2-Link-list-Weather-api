class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, head):
        self.head = None
        self._size = 0

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            self._size += 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        self._size += 1

    def remove_first(self):
        if(self.head == None):
            return
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            return
        curr_node = self.head
        while(curr_node.next != None and curr_node.next.next !=None):
            curr_node = curr_node.next

        curr_node.next = None



    def get_size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def print_linkedlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# test1 = Linkedlist(head = 0)
#
# test1.prepend('1')
# test1.prepend('2')
# test1.prepend('3')
# test1.prepend('4')
# test1.prepend('5')
# test1.append('6')
# test1.remove_first()
# test1.remove_last()
#
# print('The size of this linkedlist is: ', test1.get_size())
# test1.print_linkedlist()




