from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if list is at capacity
        if self.capacity > self.storage.length:
            # if not capacity add item to tail
            self.storage.add_to_tail(item)
            # set our current value as the head
            if self.storage.length == 1:
                self.current = self.storage.head
            #  if already at capacity
        else:
            self.current.value = item
            # if not at the end of the list put new item at next
            if self.current is not self.storage.tail:
                self.current = self.current.next
            # if at the end of the list then replace the head because it is the first in 
            else:
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents
        
        # ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
