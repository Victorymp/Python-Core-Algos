

class Solution:
  def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
      print(f"---- {right}: -- {s[right]} to {left}")
      s[left], s[right] = s[right], s[left]
      right -= 1
      left += 1

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)
    print(s)