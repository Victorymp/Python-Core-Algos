

class Node:

  def __init__(self, key:str, data):
    self.data = data
    self.key:str = key
    self.next:Node = None

  def toString(self):
    return self.data


class LinkedList:

  def __init__(self):
    self.head = None

  def pop(self) -> Node:
    result = self.head
    ## Set the new head 
    self.head = self.head.next
    return result

  def insertAt(self, node:Node, position:int):
    if position == 1:
      node.next = self.head
      self.head = node
      return self.head

    if self.head is None:
      self.head = node
      return self.head

    if self.head.next is None:
      self.head.next = node
      return self.head.next

    curr = self.head

    for _ in range(position - 2):
      if curr.next == None:
        break
      else:
        curr = curr.next
    node.next = curr.next
    curr.next = node
    return self.head

  def insert(self, node:Node):
    curr:Node = self.head
    while True:
      if curr.next is None:
        curr.next = node
        return curr.next
      curr = curr.next

  def deleteAt(self, key:str):
    curr = self.head
    if curr.key == key:
      self.head = curr.next
      print("Found at the front")
      return 0
    prev = self.head
    ## Get the item
    while True:
      if curr.key == key:
        prev.next = curr.next
        break 
      if curr.next:
        prev = curr
        curr = curr.next
        print(curr.key)
      else:
        print("Could not find")
        break      
    print(curr.data)      

  

  def toString(self) -> str:
    curr = self.head
    result = f"{curr.key}:{curr.data}"
    while curr.next != None:
      result = result + (f" -> {curr.next.key}:{curr.next.data}")
      curr = curr.next
    return result

if __name__ == "__main__":

  linked = LinkedList()

  node1 = Node("Node 1","Hello")
  node2 = Node("Node 2"," Cold")
  node3 = Node("Node 3","World")
  print("----------")
  linked.insertAt(node1, 1)
  linked.insertAt(node2, 3)
  linked.insertAt(node3, 2)

  print(linked.toString())
  print("----------")
  print(linked.pop().data)
  print(linked.toString())
  print("----------")

  linked.deleteAt(node3.key)
  print(linked.toString())
  print("----------")
  linked.insert(node3)
  print(linked.toString())
  print("----------")


