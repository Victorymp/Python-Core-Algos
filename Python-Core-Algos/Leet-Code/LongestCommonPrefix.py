from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
  ## First attempt within a hour
  if len(strs) == 0:
    return ""
  result = strs.pop(0)
  while len(strs) > 0:
    pnt = strs.pop(0)
    idx = 0 
    while len(pnt[:len(result)]) > idx and idx <len(result):
      ## Check if char is new
      if pnt[idx] != result[idx]:
        ## Delete everything after this item
        break
      idx+=1
    result = result[:idx]
    
  print(result)
  

def main():
  strs = ["flower","flow","flight"]
  longestCommonPrefix(strs)
  strs = ["dog","racecar","car"]
  longestCommonPrefix(strs)


if __name__ == "__main__":
    main()

        