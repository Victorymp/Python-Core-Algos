## An LRU (Least Recently Used) cache 
#  is a data storage structure that holds a limited number of items and automatically deletes the oldest, 
#  least-accessed item whenever the cache becomes full

from DataStructures import LinkedList
class LRU:

  def __init__(self, size:int):
    self.size = size
    ## Using a dict because lookup, insertion and deletion is O(1)
    self.cacheDict = {}

    ## Hashmap
    self.hash_table = [[] for _ in range(size)]

    ## Linked list
    ## Implementing it by via a queue
    self.cache = LinkedList()

  def set_val(self, key, val):
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]

    for index, (record_key, _) in enumerate(bucket):
      if record_key == key:
        bucket[index] = (key, val)
        return
    bucket.append((key, val))
    
  def add(self, item:str):
    ## check if we are at the end and we are still trying to add
    ## If full then add to the end
    if len(self.cacheDict) == self.size:
      end = self.size -1
      self.cacheDict[end] = item
      return 0

    self.cacheDict[len(self.cacheDict)] = item
    return 0

  def getItem(self, key:str) -> str:
    result = self.cacheDict[key]
    self.righShiftDict(key)
    return result
  
  def righShiftDict(self, startKey:int):
    listIter = iter(self.cacheDict)
    prev = self.cacheDict[startKey]
    for i in range(startKey+1):
      ## get the current node 
      curr = self.cacheDict[i]
      ## update the current node with the previous
      self.cacheDict[i] = prev
      ## Check if there is next
      if next(listIter,None) == None:
        break
      ## previous node now becomes current
      prev = curr

if __name__ == "__main__":
  cache = LRU(4)
  cache.add("h")
  cache.add("e")
  cache.add("l")
  cache.add("o")
  cache.add("s")

  cache.getItem(2)

  cache.add("p")

  print(cache.cacheDict)



