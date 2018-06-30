def invertir(self):
    while self.head.next:
        aux=self.head
        while aux.next.next:
            aux=aux.next
        aux.next.next=aux
        aux.next=None

    aux=self.head
    self.head=self.last
    self.last=aux