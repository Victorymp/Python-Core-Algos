def binarySearchImplementation(nums1:list[int], m:int)->int:
  pntL:int = 0

  pntR:int = len(nums1) -1

  while pntL <= pntR:
    pntM:int = pntL+(pntR - pntL)//2
    print(pntM)
    ## Base case
    if nums1[pntM] == m :
      return pntM
    
    ## To the right of the mid point
    elif m > nums1[pntM]:
      ## Get rid of the left hand side and remove the mid point from consideration
      pntL = pntM + 1
    else:
      pntR = pntM -1
  return -1



def main():
  nums1 = [-1,0,3,5,9,12]
  m =9
  print(binarySearchImplementation(nums1, m))

  nums1 = [-1,0,3,5,9,12]
  m = 2
  print(binarySearchImplementation(nums1, m))

if __name__ == "__main__":
  main()