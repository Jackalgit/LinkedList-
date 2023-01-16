class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.beg = None

    def insert_start(self, data):
        node = Node(data)
        node.next = self.beg
        self.beg = node

    def insert_after(self, aft, data):
        if self.beg is None:
            print('List is empty, insertion not possible')
        else:
            n = self.beg
            while n is not None:
                if n.data == aft:
                    break
                n = n.next
            if n is None:
                print('not element in list')
            else:
                node = Node(data)
                node.next = n.next
                n.next = node

    def insert_end(self, data):
        n = self.beg
        while n.next is not None:
            n = n.next
        node = Node(data)
        node.next = n.next
        n.next = node

    def pop(self):
        if self.beg is None:
            print('List is empty, not element to pop')
        else:
            x = self.beg.data
            self.beg = self.beg.next
            print(x)

    def del_end(self):
        if self.beg is None:
            print('List is empty, not element to delete')
            return
        if self.beg.next is None:
            self.beg = self.beg.next
        else:
            n = self.beg
            while n.next.next is not None:
                n = n.next
            n.next = n.next.next

    def del_value(self, del_data):
        if self.beg is None:
            print('List is empty, not element to delete')
            return
        if self.beg.next is None:
            if self.beg.data == del_data:
                self.beg = self.beg.next
            else:
                print('not element in list')
            return
        if self.beg.data == del_data:
            self.beg = self.beg.next
            return
        n = self.beg
        while n.next.next is not None:
            if n.next.data == del_data:
                break
            n = n.next
        if n.next.next is not None:
            n.next = n.next.next
        else:
            if n.next.data == del_data:
                n.next = n.next.next
            else:
                print('not element in list')

    def print_list(self):
        n = self.beg
        list = []
        while n is not None:
            list.append(n.data)
            n = n.next
        print(list, end=' ')

    def revers_list(self):
        if self.beg is None:
            print('List is empty')
            return
        p = self.beg
        q = None
        while p is not None:
            p.next, q, p = q, p, p.next
        self.beg = q

        # p = self.beg
        # q = p.next
        # p.next = None
        # while q is not None:
        #     t = q.next
        #     q.next = p
        #     p = q
        #     q = t
        # self.beg = p


a = LinkedList()
a.insert_start(4)
a.insert_start(7)
a.insert_start(77)
a.insert_start(2)
# a.print_list()
# [2, 77, 7, 4]
a.insert_after(7, 44)
# a.print_list()
# [2, 77, 7, 44, 4]
a.insert_end(55)
# a.print_list()
# [2, 77, 7, 44, 4, 55]
a.pop()
# 2
# a.print_list()
# [77, 7, 44, 4, 55]
a.del_end()
# a.print_list()
# [77, 7, 44, 4]
a.del_value(7)
# a.print_list()
#[77, 44, 4]
a.del_value(3435)
# not element in list
a.insert_start(33)
a.print_list()
a.revers_list()
a.print_list()
