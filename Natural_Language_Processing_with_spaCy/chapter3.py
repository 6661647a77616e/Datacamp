# Load a blank spaCy English model and add a sentencizer component
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")


# Create Doc containers, store sentences and print its number of sentences
doc = nlp(texts)
sentences = [s for s in doc.sents]
print("Number of sentences: ", len(sentences), "\n")


# Print the list of tokens in the second sentence
print("Second sentence tokens: ", [token for token in sentences[1]])




#Analyzing Pipeliness in Spacy



# Load a blank spaCy English model
nlp = spacy.blank("en")


# Add tagger and entity_linker pipeline components
nlp.add_pipe("tagger")
nlp.add_pipe("entity_linker")


# Analyze the pipeline
analysis = nlp.analyze_pipes(pretty=True)
