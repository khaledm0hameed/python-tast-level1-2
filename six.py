#Create a function that takes a sentence and word and remove the word from the sentence
def remove_word(sentence: str, word: str):
    new_sentence = " ".join([w for w in sentence.split() if w != word])
    return new_sentence
