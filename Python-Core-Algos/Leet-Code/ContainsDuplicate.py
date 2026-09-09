

class Solution:

  def containsDuplicate(nums: list):
    ## Given an integer array nums, return true if any value appears at
    #  least twice in the array, and return false if every element is distinct.
    if len(nums) == 1:
      return False
    if len(nums) == 2:
      return nums[0] == nums[len(nums) -1]
    if nums[0] == nums[len(nums) -1]:
      return True
    seen = {}

    for i in nums:
      if i in seen:
        return True
      seen.update({i:1})

    return False
  
  def containsDuplicate2(nums: list):
    nume_set = set()

    for i in nums:
      if i in nume_set:
        return True
      else:
        nume_set.add(i)
    return False

      
    


if __name__ == "__main__":
  nums = [1,2,3,1]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: True")
  print(result)
  print("---------------------\n")

  nums = [1,2,3,4]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: False")
  print(result)
  print("---------------------\n")

  nums = [1,1,1,3,3,4,3,2,4,2]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: True")
  print(result)
  print("---------------------\n")

  nums = [0,4,5,0,3,6]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: True")
  print(result)
  print("---------------------\n")

  nums = [1,5,-2,-4,0]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: False")
  print(result)
  print("---------------------\n")

  nums = [2,14,18,22,22]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: True")
  print(result)
  print("---------------------\n")

  nums = [1000000000,1000000000,11]
  result = Solution.containsDuplicate(nums)
  print("-------Result--------")
  print(f"Inputs: {nums}")
  print("Expected: True")
  print(result)
  print("---------------------\n")
