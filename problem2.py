"""
Extracting a Substring from a Sentence
Objective: Given a sentence, extract and print a specific word using string slicing.
sentence = "The quick brown fox jumps over the lazy dog"
extract third word "brow"
"""

sentence = "The quick brown fox jumps over the lazy dog"

word = "brow"

word_index = sentence.find(word)

extracted_word = sentence[word_index: word_index + len(word)] 

print(sentence)
print(f'Sliced String: {extracted_word}')