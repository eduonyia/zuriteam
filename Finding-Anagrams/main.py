# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # sort
    word = sorted(word)
    anagram = sorted(anagram)

    if(word== anagram):
        # print("Both are anagrams.")
        return True
    else:
        # print("Both aren't anagrams.")
        return False

    

state = find_anagram("hello", "check")
print(state)

