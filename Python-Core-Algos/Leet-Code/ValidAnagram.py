

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        """
        ### using a dict as a data type 
        ### for char in s if char is new then add to the list as 1 else plus 1 to char
        if len(s) != len(t):
            return False

        sDict = self.dictionary(list(s))
        tDict = self.dictionary(list(t))
        result = []
        for i in tDict:
            if i in sDict.keys():
                if sDict[i] == tDict[i]:
                    result.append(True)
                else:
                    result.append(False)
            else:
                result.append(False)
        
        if False in result:
            return False
        
        return True
        

    def dictionary(self,s:list) -> dict:
        letter = {}
        for char in list(s):
            if char in letter:
                letter.update({char: letter[char]+1})
            else:
                letter.update({char:1})
        return letter


if __name__ == "__main__":

  s = "anagram"
  t = "nagaram"
  result = Solution.isAnagram(s,t)
  print("-------Result--------")
  print(f"Inputs: {s} -- {t}")
  print(result)
  print("---------------------\n")

  s = "rat"
  t = "car"
  result = Solution.isAnagram(s,t)
  print("-------Result--------")
  print(f"Inputs: {s} -- {t}")
  print(result)
  print("---------------------\n")