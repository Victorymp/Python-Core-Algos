# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
  def reverse(self, x: int) -> int:
    xString = str(x)
    result = ""
    end = len(xString) - 1
    for i in range(len(xString)):
      result = result + xString[end - i]
    if result[end] == "-":
      result = "-" + result[:end]
    fin = int(result)
    if fin < pow(-2,31) or fin > pow(2,31)-1:
      return 0
    return fin

if __name__ == "__main__":

  x = 123
  result = Solution().reverse(x)
  print("-------Result--------")
  print(f"Inputs: 123")
  print(result)
  print(f"Expected: 321")
  print("---------------------\n")

  x = -123
  result = Solution().reverse(x)
  print("-------Result--------")
  print(f"Inputs: -123")
  print(result)
  print(f"Expected: -321")
  print("---------------------\n")

  x = 120
  result = Solution().reverse(x)
  print("-------Result--------")
  print(f"Inputs: 120")
  print(result)
  print(f"Expected: 21")
  print("---------------------\n")

  x = 900000
  result = Solution().reverse(x)
  print("-------Result--------")
  print(f"Inputs: 900000")
  print(result)
  print(f"Expected: 9")
  print("---------------------\n")

  x = 1463847412
  result = Solution().reverse(x)
  print("-------Result--------")
  print(f"Inputs: 1463847412")
  print(result)
  print(f"Expected: 2147483641")
  print("---------------------\n")