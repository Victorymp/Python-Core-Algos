## An LRU (Least Recently Used) cache 
#  is a data storage structure that holds a limited number of items and automatically deletes the oldest, 
#  least-accessed item whenever the cache becomes full
class LRU:

  def __init__(self, size:int):
    self.size = size
    self.cacheList = [[] for _ in range(size)]

  def add(self, key:str, item:str):
      ## check if we are at the end and we are still trying to add
    if len(self.cacheList[self.size -1]) > 0:
      self.cacheList[self.size -1] = [key, item]

    for i in range(len(self.cacheList)):
      if len(self.cacheList[i]) == 0:
        ## This always a
        self.cacheList[i] = [key, item]
        break
    print(self.cacheList)
    ## Check items in list 

  def getItem(self, key:str) -> str:

    for i in range(len(self.cacheList)):
      if self.cacheList[i][0] == key:
        result = self.cacheList[i]
        self.rightShift(i-1, result)
        return result

  def rightShift(self, start:int , startItem:list):
    listIter = iter(self.cacheList)
    prev = startItem
    for i in range(len(self.cacheList) - start):
      ## get the current node 
      curr = self.cacheList[i]
      ## update the current node with the previous
      self.cacheList[i] = prev
      ## Check if there is next
      nextItem = next(listIter, None)
      if nextItem == None:
        break
      ## previous node now becomes current
      prev = curr

if __name__ == "__main__":
  cache = LRU(4)
  cache.add("h1","h")
  cache.add("e1","e")
  cache.add("l1","l")
  cache.add("o1","o")
  cache.add("s1","s")

  cache.getItem("l1")

  cache.add("p1","p")



