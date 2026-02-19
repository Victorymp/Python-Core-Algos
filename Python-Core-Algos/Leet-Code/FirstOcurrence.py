
def strStr(haystack: str, needle: str) -> int:
  if needle == "":
    return -1
  count = 0
  pnt = haystack
  while len(pnt) >= len(needle):
    ocurrences = 0 
    ## Check the next 3
    for i in pnt[:len(needle)]:
      ## If it is different
      if i != needle[ocurrences]:
        break
      if ocurrences == len(needle)-1:
        return count
      ocurrences += 1 
    count +=1
    pnt = haystack[count:]
  return -1

def optimal(haystack: str, needle: str) -> int:
  return haystack.find(needle)

def main():
  haystack = "sadbutsad"
  needle = "sad"
  print(strStr(haystack,needle))

  haystack = "leetcode"
  needle = "leeto"
  print(strStr(haystack,needle))

  haystack = "butsad"
  needle = "sad"
  print(strStr(haystack,needle))

  haystack = "butsa"
  needle = "sad"
  print(strStr(haystack,needle))

  haystack = "mississippi"
  needle = "issip"
  print(strStr(haystack,needle))


if __name__ == "__main__":
  main()