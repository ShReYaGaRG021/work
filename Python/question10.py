import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from collections import defaultdict

def count_pos(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Initialize counters for different parts of speech
    pos_counts = defaultdict(int)
    
    # Process each sentence
    for sentence in sentences:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Perform part-of-speech tagging on the words
        tagged_words = pos_tag(words)
        
        # Count the number of verbs, nouns, pronouns, and adjectives
        for word, tag in tagged_words:
            if tag.startswith('VB'):  # Verb
                pos_counts['verbs'] += 1
            elif tag.startswith('NN'):  # Noun
                pos_counts['nouns'] += 1
            elif tag.startswith('PR'):  # Pronoun
                pos_counts['pronouns'] += 1
            elif tag.startswith('JJ'):  # Adjective
                pos_counts['adjectives'] += 1
    
    return pos_counts

# Test the function with example phrases
text1 = "I love eating pizza."
text2 = "The cat sat on the mat and looked cute."

# Count the parts of speech in the given texts
result1 = count_pos(text1)
result2 = count_pos(text2)

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)

