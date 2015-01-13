

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text
#file containing over five-thousand first names, begin by sorting it 
#into alphabetical order. Then working out the alphabetical value for
#each name, multiply this value by its alphabetical position in the list
#to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, 
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?
import string
from collections import OrderedDict

def read_names(filename):
    with open(filename, 'r') as f:
        names = f.readline()
        return names.replace("\"", '')

def get_score(word):
    score = 0
    for letter in word:
        score += alpha[letter]
    return score

def total(word):
    return ord_names[word] * (key_list.index(word) + 1)

unsorted_names = read_names('../data/p022_names.txt')
ndict = {}
alpha = {}

# for score
for index, letter in enumerate(string.ascii_uppercase):
    alpha[letter] = index + 1

for name in unsorted_names.split(','):
    ndict[name] = get_score(name)

# sort
ord_names = OrderedDict(sorted(ndict.items(), key=lambda d: d[0]))
# for indexing
key_list = list(ord_names.keys())

final = sum([total(x) for x in key_list])
print(final)



