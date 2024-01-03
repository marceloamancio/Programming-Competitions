m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }


def generate_candidates(digits, candidate):
  if len(candidate) < len(digits):
    return m[digits[len(candidate)]]

  return ""

# def backtrack(candidate, data)
def backtrack(digits, candidate):
  if len(candidate) == len(digits): # is a solution
    solution.append(candidate) # process solution
    return 

  for next_candidate in generate_candidates(digits, candidate):
    backtrack(digits, candidate + next_candidate)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        global solution 
        solution = []
        candidate = ""

        if not digits:
            return []

        backtrack(digits, candidate)

        return solution
        