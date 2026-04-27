class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Lista:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    
    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

    def buscarNodo(self, objetivo):
        actual = self.head
        while actual is not None:
            if actual.data == objetivo:
                return True
            actual = actual.next
        return False

    def borrarPrimerNodo(self):
        if self.head is not None:
            self.head = self.head.next

    def eliminar_por_valor(self, dato):
        if self.head is None:
            return

        if self.head.data == dato:
            self.head = self.head.next
            return

        anterior = self.head
        actual = self.head.next

        while actual is not None:
            if actual.data == dato:
                anterior.next = actual.next
                return
            anterior = actual
            actual = actual.next

    def tamano(self):
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    def invertir(self):
        anterior = None
        actual = self.head

        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

        self.head = anterior

    def ordenar(self):
        if self.head is None:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.head

            while actual.next is not None:
                if actual.data > actual.next.data:
                    temp=actual.data
                    actual.data = actual.next.data
                    actual.next.data = temp
                    cambiado = True
                actual = actual.next

    def ordenar(self):
        if self.head is None:
            return

        cambiado = True

        while cambiado:
            cambiado = False
            prevAnterior = None  
            anterior = self.head 
            actual = self.head.next  

            while actual is not None:
                if anterior.data > actual.data:

                    if prevAnterior is not None:
                        prevAnterior.next = actual
                    else:
                        self.head = actual  

                    anterior.next = actual.next

                    actual.next = anterior

                    prevAnterior = actual  
                    actual = anterior.next 
                    cambiado = True

                else:
                    prevAnterior = anterior
                    anterior = actual
                    actual = actual.next

    def jose(self,k):
        A=1j = 1
        prev = None

        # avanzar k-1 veces
        while j < k:
            prev = actual
            actual = actual.next
            j += 1

        # eliminar nodo actual
        prev.next = actual.next
        actual = actual.next
        n -= 1
        n=0
        t=self.head
        actual=self.head.next
        while actual !=self.head:
            if t ==self.head:
                n += 1
                t=None
            actual=actual.next
            n +=1 
        actual=self.head
        while n !=1:
            j=0
            while j<k:
                j +=1
                temp=actual
                actual=actual.next
                actual.next=temp
                if j==k:
                    temp=A
                    A=None
                    actual=temp.next
                    n -=1
