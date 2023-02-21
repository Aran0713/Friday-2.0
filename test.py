import nltk
from nltk.corpus import wordnet

syns=wordnet.synsets('the')[0]
type(syns)

print(syns.definition(), syns.examples(), syns.pos())
