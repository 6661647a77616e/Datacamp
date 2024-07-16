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

-------------------------------------------
#\  Word Vector Projection

words = ["tiger", "bird"]

# Extract word IDs of given words
word_ids = [nlp.vocab.strings[w] for w in words]

# Extract word vectors and stack the first five elements vertically
word_vectors = np.vstack([nlp.vocab.vectors[i][:5] for i in word_ids])

# Calculate the transformed word vectors using the pca object # Project into 2D space
pca = PCA(n_components=2)
word_vectors_transformed = pca.fit_transform(word_vectors)

# Print the first component of the transformed word vectors
print(word_vectors_transformed[:, 0])

------------------------------------------
#Similar words in vocabulary

# Find the most similar word to the word computer
most_similar_words = nlp.vocab.vectors.most_similar(np.asarray([word_vector]), n = 1)

# Find the list of similar words given the word IDs
words = [nlp.vocab.strings[w] for w in most_similar_words[0][0]]
print(words)

--------------------------------------------

#// Doc similarity with spaCy
# Create a documents list containing Doc containers
documents = [nlp(t) for t in texts]

# Create a Doc container of the category
category = "canned dog food"
category_document = nlp(category)

# Print similarity scores of each Doc container and the category_document
for i, doc in enumerate(documents):
  print(f"Semantic similarity with document {i+1}:", round(doc.similarity(category_document), 3))

----------------------------------------------------

#Span similarity with spaCy
# Create a Doc container for the category
category = "canned dog food"
category_document = nlp(category)

# Print similarity score of a given Span and category_document
document_span = document[0:3]
print(f"Semantic similarity with", document_span.text, ":", round(document_span.similarity(category_document), 3))

--------------------------------------------------------

#Semantic similarity for categorizig texts
# Populate Doc containers for the word "sauce" and for "texts" string
key = nlp("sauce")
sentences = nlp(texts)

# Calculate similarity score of each sentence and a Doc container for the word sauce
semantic_scores = []
for sent in sentences.sents:
	semantic_scores.append({"score": round(sent.similarity(key), 2)})
print(semantic_scores)





