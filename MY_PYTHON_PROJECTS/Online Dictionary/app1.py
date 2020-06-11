import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def wordmeaning(word):
    word = word.lower()
    length = len(difflib.get_close_matches(word, data.keys()))
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]   

    elif word.upper() in data:
        return data[word.upper()] 

    elif length > 0 : 
        print (f"Do you mean {difflib.get_close_matches(word, data.keys())[0]}") 
        choice = input("Enter Y for Yes and N for No.")
        if choice.upper() == 'Y':
            new = difflib.get_close_matches(word, data.keys())[0]
            return data[new]
        else:
            return ["Word does not exist. Please try again."] 

    else:
        return ["Are you sure that's the word?? It does not exists!! "]
        
    

word = input("Enter a word: ")    
result = (wordmeaning(word))
for r in result:
    print (r)
