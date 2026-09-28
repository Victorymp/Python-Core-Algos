## An LRU (Least Recently Used) cache 
#  is a data storage structure that holds a limited number of items and automatically deletes the oldest, 
#  least-accessed item whenever the cache becomes full
class LRU:

  def __init__(self, size:int):
    self.size = size
    self.cacheList = [[],[] for _ in range(size)]

  def add(self, key:str, item:str):
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
        ## This is now the most recently used item
        temp = self.cacheList[i]

        front = self.cacheList[0]
        ## right shift
        for i in range
        self.cacheList[0] = temp

        ## Put this one
  def swapItems(self, key1:str, key2:str):
    temp1:int = -1
    temp2:int = -1
    for i in range(self.size -1 ):
      if self.cacheList[i][0] == key1:
        temp1 = i
      if self.cacheList[i][0] == key2:
        temp2 = i
      if temp1 != -1 and temp2 != -1:
        self.cacheList[temp1][0], self.cacheList[temp2][0] = self.cacheList[temp2][0], self.cacheList[temp1][0]


  def rightShift(self, front:list):
    listIter = iter(self.cacheList)
    prev = None
    for i in range(self.cacheList):
      curr = self.cacheList[i][0]
      if i == 0:
        prev = self.cacheList[i][0]
      nextItem = next(listIter, None)
      if nextItem != None:
        nextItem = prev 
      prev = curr


if __name__ == "__main__":
  cache = LRU(4)
  cache.add("h")
  cache.add("e")
  cache.add("l")
  cache.add("0")
  cache.add("s")



