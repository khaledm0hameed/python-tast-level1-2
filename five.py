#Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)
def count_sentences(sentences:str):
    word=sentences.split()
    return len(word)

