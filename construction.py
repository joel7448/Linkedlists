class Node:

  def __init__(self, value=None):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.length = 0

  def append(self, newdata):
    NewNode = Node(newdata)
    if self.head is None:
      self.head = NewNode
    else:
      laste = self.head
      while (laste.next):
        laste = laste.next
      laste.next = NewNode
    self.length += 1

  def list_traversal(self, index):
    counter = 0
    currNode = self.head
    while (counter != index):
      currNode = currNode.next
      counter += 1
    return currNode

  def insert(self, index, newData):
    NewNode = Node(newData)
    curr = self.head
    if index < self.length:
      if index > 0:
        curr = self.list_traversal(index - 1)
        NewNode.next = curr.next
        curr.next = NewNode
      else:
        self.prepend(newData)
      self.length += 1
    else:
      self.append(newData)

  def prepend(self, value):
    newNode = Node(value)
    if self.head is Node:
      self.head = newNode
    else:
      curr = newNode
      curr.next = self.head
      self.head = curr

    self.length += 1

  def remove(self,index):
    curr = self.head;
    if index>0:
      curr = self.list_traversal(index-1);
      curr.next = curr.next.next;
    elif index==0:
      self.head = self.head.next;
      

  def display(self):
    curr = self.head
    while (curr is not None):
      print(curr.value)
      curr = curr.next


ll = LinkedList() # Initiates a linked list 
ll.append(10)     # appends 10 to the end of linkedlist        # null-->10
ll.append(50)     # appends 50 to the end of linkedlist        # null-->10-->50   
ll.insert(0, 179) # Inserts 179 at the index 0                 # null-->179-->10-->50 
ll.prepend(220)   # prepends 220 at the begining of linkedlist # null-->220-->179-->10-->50
ll.remove(2)      # removes index 2                            # null-->220-->179-->50
ll.append(90)     # appends 90 at the end of linkedlists       # null-->220-->179-->50-->90
ll.display()      # displays every element in the linkedlists  

