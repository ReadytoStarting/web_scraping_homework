import re
pattern = r'^[\w]'
def count_words(sentence):
    word = sentence.split()
    return len(word)

sentence = input('write sentence :')
count = count_words(sentence)
print(count)