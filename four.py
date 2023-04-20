#Create a function that takes a sentence and prints the sentence without duplicated words
def remove_duplicates(sentence: str):
    word=sentence.split(" ")
    new_word=[]
    for word in word:
        if word not in new_word:
            new_word.append(word)
    new_word=" ".join(new_word)    
    return new_word


