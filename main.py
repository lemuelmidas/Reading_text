# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string
import collections
from pathlib import *

file_folder= Path.cwd().joinpath(Path("story.txt"))
print(file_folder)
file_to_open= file_folder

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        file_content= file.read()
    
    return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text= text.translate(str.maketrans("", "", string.punctuation))
    word_count= {}
    split_text= text.split()

    #for word in split_text:
    #    word_count[word]=split_text.count(word)    

    #for word in split_text:
    #    if word not in word_count:
    #        word_count[word]=0
    #    word_count[word] += 1

    #for word in split_text:
    #    if word in word_count:
    #        word_count[word] += 1
    #    else:
    #       word_count[word] = 1

    #for word in split_text:
    #   word_count[word] = word_count.get(word, 0) +1

    word_count= collections.Counter(split_text)
    word_count= {k: v for k,v in word_count.items()}
    return dict(word_count)
    
    
        
        
    #return word_count
        

print(count_words())
