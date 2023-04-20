#Create a function takes a sentence and a word and prints how many time the word used in the sentence
def count_word(sentence: str, word: str):
    word_count = 0
    for w in sentence.split():
        if w == word:
            word_count += 1
    print(f"The word '{word}' appears {word_count} times in the sentence.")
