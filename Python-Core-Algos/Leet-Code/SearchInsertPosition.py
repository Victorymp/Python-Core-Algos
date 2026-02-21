from typing import List

def searchInsert(nums: List[int], target: int) -> int:
  if len(nums) == 1:
    if nums[0] < target: return 1
    else: return 0 
  nms = iter(nums)
  idx = 0 
  print("-------Target-------")
  print(target)
  print("-------Run-----------")

  while True:
    try:
        nx = next(nms)
        pnt = nums[idx]
        print(f"{pnt} - {target} - {nx}")
        if pnt ==  target:
           return idx
        if nx > target:
           return idx
        idx +=1
    except StopIteration:
        break

  return len(nums)

def srcInsert(nums: List[int], target: int) -> int:
  if len(nums) == 1:
    if nums[0] < target: return 1
    else: return 0 
  nms = iter(nums)
  idx = 0 

  while True:
    try:
      nx = next(nms)
      pnt = nums[idx]
      if pnt ==  target:
          return idx
      if nx > target:
          return idx
      idx +=1
    except StopIteration:
      break

  return len(nums)

def optimal(nums: List[int], target: int) -> int:
  left, right = 0, len(nums)-1
  while left <= right:
      mid = (left+right)//2
      if nums[mid] == target:
          return mid
      if nums[mid] > target:
          right = mid-1
      else:
          left = mid+1
  return left

def main():
  nums = [1,3,5,6]
  target = 5
  result = searchInsert(nums,target)
  print("-------Result--------")
  print(result)
  print("---------------------\n")

  nums = [1,3,5,6]
  target = 2
  result = searchInsert(nums,target)
  print("-------Result--------")
  print(result)
  print("---------------------\n")

  nums = [1,3,5,6]
  target = 7
  result = searchInsert(nums,target)
  print("-------Result--------")
  print(result)
  print("---------------------\n")

if __name__ == "__main__":
  main()