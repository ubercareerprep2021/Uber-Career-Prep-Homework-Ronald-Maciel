# -*- coding: utf-8 -*-

# check if s1 is permutation of s2 
# examples:
#    isStringPermutation(s1: “asdf”, s2: “fsda”) == true
#    isStringPermutation(s1: “asdf”, s2: “fsa”) == falsek
#    isStringPermutation(s1: “asdf”, s2: “fsax”) == false

def isStringPermutation(s1: str, s2: str) -> bool:
    if not s1 or not s2:     # if both are empties
        return True
    elif len(s1) != len(s2): # if they aren't the same size
        return False
    else:
        s1_sorted = "".join(sorted(s1))
        s2_sorted = "".join(sorted(s2))
        if s1_sorted == s2_sorted:
            return True
        else:
            return False


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    list_pairs = []

    for n in range(0, len(inputArray)):
        for m in range(n+1, len(inputArray)):
            if inputArray[n] + inputArray[m] == targetSum:
                list_pairs.append((inputArray[n], inputArray[m]))

    return list_pairs


if __name__ == '__main__':
    str1 = "test"
    str2 = "ttse"
    if isStringPermutation(str1, str2):
        print("Yes")
    else:
        print("No")
    

    inputArray = [1, 2, 3, 4, 5]
    list_pairs = pairsThatEqualSum(inputArray, 7)
    print(list_pairs)
    


