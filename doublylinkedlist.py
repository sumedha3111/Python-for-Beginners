class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None

    def insertfront(self, data):
        newnode = node(data)
        if (self.head is not None):
            self.head.prev = newnode
            newnode.next = self.head
        self.head = newnode

    def insertend(self, data):
        newnode = node(data)
        newnode.next = None
        if self.head is None:
            self.head = newnode
            return
        t = self.head
        while (t.next is not None):
            t = t.next
        t.next = newnode
        newnode.prev = t

    def insertAfter(self, data, x):
        newnode = node(data)
        if (self.head):
            l = self.head
            while (l and l.data != x):
                l = l.next
            if (l.data == x):
                newnode.next = l.next
                l.next = newnode

    def deletefront(self):
        if (self.head):
            t = self.head
            self.head = t.next
            del t
        if(self.head):
            self.head.prev = None

    def display(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next

    def deleteEnd(self):
        if (self.head):
            t = self.head
            while (t.next and t.next.next):
                t = t.next
            if (t.next is None):
                self.head = None
                return
            del t.next
            t.next = None

    def deleteAfter(self, x):
        if (self.head):
            l = self.head
            while (l and l.data != x):
                l = l.next
            if (l and l.next.next and l.data == x):
                l.next = l.next.next
                t = l
                l = l.next
                l.prev = t
            elif (l):
                l.next = None


dll = DLList()
while (1):
    print("1.insert front")
    print("2.insert back")
    print("3.insert after ")
    print("4.delete")
    print("5.delete end")
    print("6. delete after")
    print("7.display")
    print("8exit")
    ch = input("enter your choice:")
    if ch == "1":
        x = int(input("enter the data"))
        dll.insertfront(x)
    elif ch == "2":
        x = int(input("enter the data"))
        dll.insertend(x)
    elif ch == "3":
        x = int(input("Enter data:"))
        a = int(input("Enter data before:"))
        dll.insertAfter(x, a)
    elif ch == "4":
        dll.deletefront()
    elif ch == "5":
        dll.deleteEnd()
    elif ch == "6":
        x = int(input("Enter data before:"))
        dll.deleteAfter(x)
    elif ch == "7":
        dll.display()
    elif ch == "8":
        break
