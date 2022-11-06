import spacy
nlp = spacy.load('output/model-last/')  # load the model

#sentence = 'What is time complexity of binary sort algorithm'
sentence = 'tell me the bigger of the two: O(2n) and O(log n)'

doc = nlp(sentence)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)