import nltk
from nltk.corpus import words
from nltk.metrics.distance import (
    edit_distance,
    jaccard_distance,
    )
from nltk.util import ngrams
nltk.download('words')
import pandas
correct_spellings = words.words()
spellings_series = pandas.Series(correct_spellings)
spellings_series


def editreco(entries=['cormulent', 'incendenece', 'validrate']):

    outcomes = []
    for entry in entries:
        distances = ((edit_distance(entry,
                                    word), word)
                     for word in correct_spellings)
        closest = min(distances)
        outcomes.append(closest[1])
    return outcomes


editreco()

userinput = []
for i in range(0,3):
    word = input("threa woeds pleese: ")
    userinput.append(word)
    
userinput

editreco(userinput)