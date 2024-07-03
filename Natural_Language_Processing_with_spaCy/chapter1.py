
----------------------------------
# Load en_core_web_sm model as nlp
nlp = spacy.load("en_core_web_sm")

# Run an nlp model on each item of texts and append the Doc container to documents
documents = []
for text in texts:
  documents.append(nlp(text))
  
# Print the token texts for each Doc container
for doc in documents:
  print([token.text for token in doc])
-----------------------------------
#Lemmatization with spaCy

document = nlp(text)
tokens = [token.text for token in document]

# Append the lemma for all tokens in the document
lemmas = [token.lemma_ for token in document]
print("Lemmas:\n", lemmas, "\n")

# Print tokens and compare with lemmas list
print("Tokens:\n", tokens)

#token.lemma gives number representation
------------------------------------

#Sentence Segmentation with spaCy

# Generating a documents list of all Doc containers
documents = [nlp(text) for text in texts]

# Iterate through documents and append sentences in each doc to the sentences list
sentences = []
for doc in documents:
  sentences.append([s for s in doc.sents])
  
# Find number of sentences per each doc container
print([len(s) for s in sentences])


-----------------------------------
# POS Tagging
verb_sent = ""
print([(token.text, token.pos_, spacy.explain(token.pos_)) for token in nlp(verb_sent)])

#NER with Spacy
import spacy
nlp = space.load("en_core_web_sm")
text = ""
doc = nlp(text)
print(([ent.text, ent.start_char, ent.end_char, ent.label) for ent in doc.ents])
print([(token.text, token.ent_type_) for token in doc])

---------------------------------------
# POS Tagging with Spacy
documents = [nlp(text) for text in texts]

# Print token texts and POS tags for each Doc container
for doc in documents:
    for token in doc:
        print("Text: ", token.text, "| POS tag: ", token.pos_)
    print("\n")
--------------------------------------
# NER with spaCy
documents = [nlp(text) for text in texts]

# Print the entity text and label for the entities in each document
for doc in documents:
    print([(ent.text, ent.label_) for ent in doc.ents])
    
# Print the 6th token's text and entity type of the second document
print("\nText:", documents[1][5].text, "| Entity type: ", documents[1][5].ent_type_)


----------------------
# Text Processing in spaCy
# Create a list to store sentences of each Doc container in documents
sentences = [[sent for sent in doc.sents] for doc in documents]

# Create a list to track number of sentences per Doc container in documents
num_sentences = [len([sent for sent in doc.sents]) for doc in documents]
print("Number of sentences in documents:\n", num_sentences, "\n")

# Record entities text and corresponding label of the third Doc container
third_text_entities = [(ent.text, ent.label_) for ent in documents[2].ents]
print("Third text entities:\n", third_text_entities, "\n")

# Record first ten tokens and corresponding POS tag for the third Doc container
third_text_10_pos = [(token.text, token.pos_) for token in documents[2]][:10]
print("First ten tokens of third text:\n", third_text_10_pos)# Create a list to store sentences of each Doc container in documents
sentences = [[sent for sent in doc.sents] for doc in documents]
