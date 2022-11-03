import spacy
nlp = spacy.load('output/model-last/')  # load the model

sentence = 'What is time complexity of binary sort algorithm'

doc = nlp(sentence)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)