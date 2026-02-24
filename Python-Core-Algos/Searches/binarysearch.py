def binarySearchImplementation(nums1:list[int], m:int)->int:
  pntL:int = 0

  pntR:int = len(nums1)-1

  while pntL < pntR:
    pntM:int = round(pntL+((pntR - pntL)/2))
    print(pntM)
    ## Base case
    if nums1[pntM] == m :
      return pntM
    
    ## To the right of the mid point
    elif m > nums1[pntM]:
      ## Get rid of the left hand side
      pntL = pntM 

    else:
      pntR = pntM 
  return -1



def main():
  nums1 = [2, 3, 4, 10, 40]
  m =3
  print(binarySearchImplementation(nums1, m))


if __name__ == "__main__":
  main()