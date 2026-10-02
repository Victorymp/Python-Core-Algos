

class Node:

  def __int__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __int__(self):
    self.head = Node(None)

  def pop(self) -> Node:
    result = self.head
    ## Set the new head 
    self.head = self.head.next
    return result

  def insert(self, node:Node, position:int):
    if position == 1:
      temp = self.head
      self.head = node
      self.head.next = temp

    curr = self.head

    for _ in range(position - 2):
      if curr.next == None:
        break
      else:
        curr = curr.next

    node.next = curr.next
    curr.next = node
    return self.head

  def toString(self):
    curr = self.head
    while curr != None:
      print(f"Data: {curr.data}, Next Node: {curr.next}")
      curr = curr.next

