
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

