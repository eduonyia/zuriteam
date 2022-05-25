# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename, "rt")
    data = file.read()
    data = data.split()

    return data


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    my_dict = {}
    count = 0

    for item in text:
        my_dict[item] = my_dict.get(item, 0) + 1
    
    # print(my_dict)



    return my_dict

print(count_words())
#text = read_file_content("./story.txt")
#print(text)
#count_words()
