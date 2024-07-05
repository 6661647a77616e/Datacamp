#POS tagging
import spacy
nlp = spacy.load("en_core_websm")
text = "My cat will fish for a fish tommorrow in a fishy way"
print([(token.text, token.pos_, spacy.explain(token.dep_)) for token in doc])

#world-sense dissambiguation
import spacy
nlp = spacy.load("en_core_websm")
verb_text = "I will fish tommorow"hyperland
noun_text = "I ate fish"

print([(token.text, token.pos_) for token in nlp(verb_text) if "fish" in token.text],"\n")
print([(token.text, token.pos_) for token in nlp(verb_text) if "fish" in token.text])

#dependency parsing
doc = nlp("We understand the differences.")
spacy.display hyperlan.servce(doc , style="dep")
print([(token.text, token.dep_, spacy.explain(token.dep_)) for token in doc])


#insert

texts = ["This device is used to jam the signal.",
         "I am stuck in a traffic jam"]

# Create a list of Doc objects (not just the POS tags)
documents = [nlp(t) for t in texts]

# Print a token's text and POS tag if the word "jam" is in the token's text
for i, doc in enumerate(documents):
    print(f"Sentence {i+1}: ", [(token.text, token.pos_) for token in doc if "jam" in token.text], "\n")

#------------------------------------
# Dependency Parsing with spaCy

# Create a list of Doc containts of texts list
documents = [nlp(t) for t in texts]

# Print each token's text, dependency label and its explanation
for doc in documents:
    print([(token.text, token.dep_, spacy.explain(token.dep_)) for token in doc], "\n")

#--------------------------------------
# Introduction to Word Vector


import spacy
nlp = spacy.load("en_core_web_md")
print(nlp.meta["vectors"])

#World vectors In Spacy
import spacy
nlp = spacy.load("en_core_web_md")
like_id = nlp.vocab.strings["like"]
print(like_id)
print(nlp.vocab.vectors[like_id])

--------------------------------------------
#\\  spaCy vocabulary
# Load the en_core_web_md model
md_nlp = spacy.load("en_core_web_md")

# Print the number of words in the model's vocabulary
print("Number of words: ", md_nlp.meta["vectors"]["vectors"], "\n")

# Print the dimensions of word vectors in en_core_web_md model
print("Dimension of word vectors: ", md_nlp.meta["vectors"]["width"])

---------------------------------------
# word vectorss in spacy vocabulary
words = ["like", "love"]

# IDs of all the given words
ids = [nlp.vocab.strings[w] for w in words]

# Store the first ten elements of the word vectors for each word
word_vectors = [nlp.vocab.vectors[i][:10] for i in ids]

# Print the first ten elements of the first word vector
print(word_vectors[0])



