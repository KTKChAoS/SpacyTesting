import spacy
from spacy.lang import en
from spacy.tokens import DocBin
from tqdm import tqdm
trainData = ("What is the time complexity of the merge Sort algorithm?",{"entities":[(35,45,"Algorithm"),(12,27,"Action")]}),
("difference between Selection sort and other sorts",{"entities":[(166,176,"Action"),(205,219,"Algorithm"),(247,258,"Algorithm")]}),
("Compare Selection Sort with other sorts",{"entities":[(0,7,"Action"),(8,22,"Algorithm"),(28,39,"Algorithm")]}),
("Selection Sort explanation",{"entities":[(0,14,"Algorithm"),(15,26,"Action")]}),
("Big O notation of selection Sort",{"entities":[(18,32,"Algorithm"),(0,5,"Action")]}),
("What is the time complexity of the Selection Sort algorithm?",{"entities":[(12,27,"Action"),(35,49,"Algorithm")]}),
("Which is bigger, O(n) or O(log(n))",{"entities":[(9,15,"Action"),(17,21,"Algorithm"),(25,34,"Algorithm")]}),
("Which is bigger, O(n) or O(log(2n))",{"entities":[(8,15,"Action"),(17,21,"Algorithm"),(25,35,"Algorithm")]}),


nlp = spacy.blank('en')  # load a new spacy model
db = DocBin()  # create a DocBin object
for text, annot in tqdm(trainData):  # data in previous format
    doc = nlp.make_doc(text)  # create doc object from text
    ents = []
    for start, end, label in annot['entities']:  # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode='contract')
        if span is None:
            print('Skipping entity')
        else:
            ents.append(span)
    try:
        doc.ents = ents  # label the text with the ents
        db.add(doc)
    except:
        print(text, annot)
db.to_disk('./train.spacy')  # save the docbin object

# python3 main.py
# python3 -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy
# python3 test.py