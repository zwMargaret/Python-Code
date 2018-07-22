

################
# namedtuple
from collections import namedtuple

Stock = namedtuple("Stock","symbol current high low")
stock = Stock("GOOG",613,high=615,low=610)



################
# dict
stocks = {"GOOG":(613,625,610),"AAPL":(30,29,31)}

stocks.get("RIM","NOT FOUND")
# return "NOT FOUND"


stocks.setdefault("GOOG","INVALID")
stocks.setdefault("RIM",(11,12,13))

for key,value in stocks.items():
    print("{} has value {}".format(key,value))




#################
# defaultdict
def letter_frequency(sentence):
    frequecies = {}
    for letter in letter_frequency:
        frequency = frequencies.setdefault(letter,0)
        frequency[letter]+=1
    return frequecies


#-----------------
from collections import defaultdict
def letter_frequency2(sentence):
    frequecies = defaultdict(int)

    for letter in sentence:
        frequecies[letter] += 1
    return frequecies


##################
from collections import defaultdict

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items,[])


#----------
d = defaultdict(tuple_counter)

d['a'][1].append('hello')
d['b'][1].append('world')
d




####################
# list
import string
CHARACTERS = list(string.ascii_letters)+[" "]

def letter_frequency3(sentence):
    frequencies = [(c,0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter,frequencies[index][1]+1)
    return frequencies



#######################
# list.sort()
x = [(1,'c'),(2,'a'),(3,'b')]
x.sort()
x.sort(key=lambda i: i[1])

l = ['hello','HELP','helo']
i.sort()
l.sort(key=str.lower)



#######################
# zip
import sys
filename = sys.argv[1]

contacts = []
with open(filename) as file:
    header = file.readline().strip().split('\t')
    for line in file:
        line = line.strip().split('\t')
        contact_map = zip(header,line)
        contacts.append(dict(contact_map))
    for contact in contacts:
        print("email: {email} -- {last}, {first}".format(**contact))

#########################
# The code above can also be written as below
import sys
filename = sys.argv[1]

with open(filename,'w') as file:
    header = file.readline().strip.split('\t')
    contacts = [dict(zip(header,line.strip().split('\t'))) for line in file]


######################
list_1 = ['a','b','c']
list_2 = [1,2,3]
zipped = zip(list_1,list_2)
zipped = list(zipped)
zipped
# should be [('a',1),('b',2),('c',3)]

unzipped = zip(*zipped)
list(unzipped)
# should be [('a','b','c'),(1,2,3)]

#######################
# enumerate

def min_max_indexes(seq):
    minimum = min(enumerate(seq),key=lambda s:s[1])    #"(index,value)"" is output of "enumerate(seq)"
    maximum = max(enumerate(seq),key=lambda s:s[1])
    return minimum[0], maximum[0]

#######################
input_strings = ['1','5','28','131','3']
output_integers = [int(num) for num in input_strings]
output_ints = [int(n) for n in input_strings if len(n)<3]


#######################
from collections import namedtuple
Book = namedtuple("Book","author title genre")
books = [Book("a",1,2),Book(...),...]

# Collections: repeated values would be removed
fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}

# dict: title is key, namedtuple is value
fantasy_titles = {b.title:b for b in books if b.genre=='fantasy'}



################################
# use ( ) instead of [ ]

with open(inname) as infile:
    with open(outname,'w') as outfile:
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)


################################
# method 1
with open(inname) as infile:
    with open(outname,'w') as outfile:
        warnings = (l.replace('\tWARNING','') for l in infile if 'WARNING'm in l)
        for l in warnings:
            outfile.write(l)

################################
# method 2
with open(inname) as infile:
    with open(outname,'w') as outfile:
        for l in infile:
            if 'WARNING' in l:
                outfile.write(l.replace('\tWARNING',''))

################################
# method 3

class WarningFilter:
    def __init__(self,insequence):
        self.insequence = insequence
    
    def __iter__(self):
        return setdefault

    def __next__(self):
        l = self.insequence.readline()
        while l and 'WARNING' not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace('\tWARNING','')


with open(inname) as infile:
    with open(outname,'w') as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)




################################
# method 4
def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yeild l.replace('\tWARNING','')


with open(inname) as infile:
    with open(outname,'w') as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)










