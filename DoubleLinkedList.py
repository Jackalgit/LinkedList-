class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        """Вставка элементов в пустой список"""

        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        """ Вставка элементов в начало.
            1. Для нового узла ссылка на следующий узел будет установлена на self.start_node.
            2. Для self.start_node ссылка на предыдущий узел будет установлена на вновь вставленный узел.
            3. Наконец, self.start_node станет вновь вставленным узлом."""

        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        """ Вставка элементов в конец.
            Если список уже содержит какой-то элемент, мы проходим по списку, пока ссылка на следующий узел
            не станет None. Когда ссылка на следующий узел становится None, это означает, что текущий узел
            является последним узлом. Предыдущая ссылка для нового узла устанавливается на последний узел,
            а следующая ссылка для последнего узла устанавливается на вновь вставленный узел."""
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        """ Вставка элемента после другого элемента.
            Мы перебираем все узлы двусвязного списка. В случае, если узел,
            после которого мы хотим вставить новый узел, не найден, мы отображаем сообщение пользователю
            о том, что элемент не найден. В противном случае, если узел найден, он выбирается, и мы
            выполняем четыре операции: Установите предыдущую ссылку вновь вставленного узла на выбранный
            узел. Установите следующую ссылку вновь вставленного узла на следующую ссылку выбранного.
            Если выбранный узел не является последним узлом, установите предыдущую ссылку следующего узла
            после выбранного узла на вновь добавленный узел. Наконец, установите следующую ссылку
            выбранного узла на вновь вставленный узел."""

        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        """ Вставка элемента перед другим элементом.
            Мы перебираем все узлы двусвязного списка. В случае, если узел,
            перед которым мы хотим вставить новый узел, не найден, мы отображаем сообщение пользователю,
            что элемент не найден. В противном случае, если узел найден, он выбирается, и мы выполняем
            четыре операции: Установите следующую ссылку вновь вставленного узла на выбранный узел.
            Установите предыдущую ссылку вновь вставленного узла на предыдущую ссылку выбранного.
            Установите следующую ссылку узла, предшествующего выбранному узлу, на только что добавленный
            узел. Наконец, установите предыдущую ссылку выбранного узла на вновь вставленный узел."""

        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def delete_at_start(self):
        """ Удаление элементов с самого начала.
            Установить значение начального узла на следующий, а затем установить для предыдущей ссылки
            начального узла значение «None». Однако, прежде чем мы это сделаем, нам нужно выполнить две
            проверки. Во-первых, нам нужно увидеть, пуст ли список. И затем мы должны увидеть, содержит
            ли список только один элемент или нет. Если список содержит только один элемент, мы можем
            просто установить для начального узла значение None. """

        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        """Удаление элементов с конца.
        Если список содержит единственный элемент, все, что нам нужно сделать, это установить для
        начального узла значение None. Если в списке более одного элемента, мы перебираем список
        до тех пор, пока не будет достигнут последний узел. Как только мы достигаем последнего узла,
        мы устанавливаем следующую ссылку узла, предшествующего последнему, на None, что фактически
        удаляет последний узел. """

        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        """Удаление элементов по значению.
        ......Если единственным элементом является тот, который мы хотим удалить, мы просто
        устанавливаем для self.start_node значение None, что означает, что теперь в списке не
        будет элемента. Если есть только один элемент, и это не тот элемент, который мы хотим
        удалить, мы просто отобразим сообщение о том, что удаляемый элемент не найден.
        Затем мы обрабатываем случай, когда список имеет более одного элемента, но элемент,
        который нужно удалить, является первым элементом. В этом случае мы просто выполняем
        логику, написанную для метода delete_at_start().
        Если список содержит несколько элементов и удаляемый элемент не является первым элементом,
        мы просматриваем все элементы в списке, кроме последнего, и смотрим, имеет ли какой-либо
        из узлов значение, соответствующее значению, которое нужно удалить. Если узел найден,
        выполняем следующие две операции: Установите значение следующей ссылки предыдущего узла на
        следующую ссылку удаляемого узла. Установите предыдущее значение следующего узла на
        предыдущую ссылку удаляемого узла. Наконец, если удаляемый узел является последним узлом,
        для следующей ссылки узла, предшествующего последнему узлу, устанавливается значение «None». """

        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def traverse_list(self):
        """Печать списка"""

        if self.start_node is None:
            print("List has not element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=" ")
                n = n.nref

    def reverse_list(self):
        """Разворот списка"""

        if self.start_node is None:
            print("List has not element")
            return
        else:
            # self.start_node.pref = self.start_node.nref
            # self.start_node.nref = None
            # while self.start_node.nref is not None:
            #     self.start_node.nref.pref = self.start_node.nref.nref
            #     self.start_node.nref.nref = self.start_node
            #     self.start_node = self.start_node.nref
            #     self.start_node.nref = self.start_node.nref.pref
            # self.start_node = self.start_node.nref

            p = self.start_node
            q = p.nref
            p.pref = q
            p.nref = None
            while q is not None:
                q.pref = q.nref
                q.nref = p
                p = q
                q = q.pref
            self.start_node = p

            # self.start_node.pref = self.start_node.nref
            # self.start_node.nref = None
            # n = self.start_node.pref
            # while n is not None:
            #     n.pref = n.nref
            #     n.nref = n.pref
            #     n = n.nref
            # self.start_node = n




mylist = DoublyLinkedList()
mylist.insert_at_start(5)
mylist.insert_at_start(40)
mylist.insert_at_end(100)
mylist.insert_at_start(1)
mylist.traverse_list()
mylist.reverse_list()
mylist.traverse_list()

