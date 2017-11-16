"""This module uses json file derived from the csv file from https://github.com/nirooj56/Nepdict/blob/master/nepdict/opt/nepdict/database/data.csv"""
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("nepali_dict.json"))

def translate(myword):
    return_stmt = "The word doesnt exist."
    if myword.lower() in data:
        #print("data[myword.lower()] = " + str(data[myword.lower()]) + " & type = " + str(type(data[myword.lower()])))
        #print("data[myword.lower()][0] = " + str(data[myword.lower()][0]) + " & type = " + str(type(data[myword.lower()][0])))
        #print("data[myword.lower()][0][\"Meaning\"] = " + str(data[myword.lower()][0]["Meaning"]) + " & type = " + str(type(data[myword.lower()][0]["Meaning"])))
        return_stmt=""
        return data[myword.lower()][0]["Meaning"]
    else:
        #similar words
        print("The word %s doesnt exist in the dictionary. Looking for similar ones..." %myword)
        similar_words = get_close_matches(myword.lower(),data.keys())
        if len(similar_words)>0:
            check_word = input("Do you mean \'%s\' instead?" %similar_words[0])
            if check_word.lower().startswith("y"):
                word = similar_words[0]
                #Creating Recursive function
                print(translate(word))
                return_stmt=""
                exit(0)
                #return_stmt = "%s = %s" %(word,data[word.lower()][0]["Meaning"])
            else:
                return_stmt = "The word %s doesn't exist." %myword
    return return_stmt

word = input("Enter word: ")

#translate(word)
print(translate(word))
