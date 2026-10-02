

class Node:

  def __init__(self, data):
    self.data = data
    self.next:Node = None

  def toString(self):
    return self.data


class LinkedList:

  def __init__(self):
    self.head = Node(None)

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

    curr = self.head

    for _ in range(position - 2):
      if curr.next == None:
        break
      else:
        curr = curr.next

    node.next = curr.next
    curr.next = node
    return self.head

  def toString(self) -> str:
    curr = self.head
    result = f"{curr.data}"
    while curr.next != None:
      result = result + (f" -> {curr.next.data}")
      curr = curr.next
    return result

if __name__ == "__main__":

  linked = LinkedList()

  node1 = Node("Hello")
  node2 = Node(" , ")
  node3 = Node("World")

  linked.insertAt(node1, 1)
  linked.insertAt(node2, 3)
  linked.insertAt(node3, 2)

  print(linked.toString())

