class Node:
     def __init__(self , k):
         self.data= k
         self.next = None
         self.prev =None

class LinkedList :
    def __init__(self):
        self.head = None
        self.last = None

    def addLast(self, k):
        newNode= Node(k)
        if self.head == None :
            self.head = self.last =  newNode
        else :
            newNode.prev=self.last
            self.last.next = newNode
            self.last =newNode

    def addFirst(self, k):
        newNode= Node(k)
        if self.head == None :
            self.head = self.last =  newNode
        else :
            newNode.next=self.head
            newNode.next.prev = newNode
            self.head =newNode


    def search(self, k):
        node = self.head
        if node!=None :
            while node!=None :
                  if node.data == k:
                     return True
                  node=node.next
        return False

    def print(self):
        node = self.head;
        while node!=None :
            print(node.data)
            node =node .next

l = LinkedList()
l.addFirst(10)
l.addLast(20)
l.addLast(30)
l.addLast(40)
l.addLast(50)
print(l.search(30))
l.print()