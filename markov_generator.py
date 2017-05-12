'''
--- Markov Generator ---

Building a module to take a .txt file as an imput and generate a markov chain of a given length

--- To Use ---

Run form_dict("text file name") to create a dictionary
Run markov_gen to create chains, give it a number for legnth of chain,
can specify a text file to generate from or give a pre-made table to avoid
re-creating the dictionary each time.

IDEA Remove punctuation, add in as an optional argument?
'''

# importing random for choice of words from the key-value list
import random
import string

# function to read a given text file, strip out punction and make lower case, returns as a large string by
# default, add quotes = True to process as a series of quotes/dialogue
def read_file(text_name, quotes = False):
    transtable = str.maketrans('', '', string.punctuation)
    if quotes == True:
        text = []
        with open(text_name + '.txt', encoding='utf8', errors='ignore') as f:
            for line in f:
                text.append(line.strip().lower().translate(transtable))
    else:
        with open(text_name + '.txt', encoding='utf8', errors='ignore') as f:
            text = f.read()
        text = text.replace('\n', ' ').lower()
        text = text.replace('-', ' ')
        text = text.translate(transtable)
    return(text)

# takes a string and forms in to a list of 3 consecutive word sequences   
def list_triples(text_name, quotes = False):
    trip_list = []
    if quotes == True:
        quote_array = read_file(text_name, quotes = True)
        for quote in quote_array:
            quote_words = quote.split()
            for i in range(len(quote_words)-2):
                trip_list.append((quote_words[i],quote_words[i+1],quote_words[i+2]))
    else:
        text_string = read_file(text_name)
        text_array = text_string.split()
        for i in range(len(text_array)-2):
            trip_list.append((text_array[i],text_array[i+1],text_array[i+2]))
    return(trip_list)

# takes a text file, forms the triples and then forms a dictionary with tuples as keys and the next word as the value
def form_dict(text_name, quotes = False):
    dictionary = {}
    triples = list_triples(text_name, quotes)
    for i in range(len(triples)):
        if (triples[i][0],triples[i][1]) not in dictionary:
            dictionary[triples[i][0],triples[i][1]] = [triples[i][2]]
        else:
            dictionary[triples[i][0],triples[i][1]].append(triples[i][2])
    return(dictionary)

# generates a markov chain of a given length, can be given a text to make a dictionary from,
# can also be given the dictionary instead to build from to avoid buiding it each time
def markov_gen(text_or_table, phrase_length, quotes = False):
    phrase = []
    if type(text_or_table) is dict:
        dic = text_or_table
    else:
        dic = form_dict(text_or_table, quotes)
    try:
        start = random.choice(list(dic))
        phrase.append(start[0])
        phrase.append(start[1])
        for i in range(phrase_length-2):
            next_word = random.choice(dic[(phrase[i],phrase[i+1])])
            phrase.append(next_word)
    except KeyError:
        markov_gen(text_or_table, phrase_length, quotes)
    for i in range(len(phrase)):
        if phrase[i] == "i":
            phrase[i] = phrase[i].upper()
    phrase[0] = phrase[0].title()
    gen_phrase = ' '.join(phrase)
    gen_phrase = gen_phrase + "."
    return(gen_phrase)

# Building the dictionaries to use for quote generation
#master = form_dict("master_quotes", quotes = True)
space_marine = form_dict("space_marine_quotes", quotes = True)
eldar = form_dict("eldar_quotes", quotes = True)
imperial_guard = form_dict("imperial_guard_quotes", quotes = True)
chaos = form_dict("chaos_quotes", quotes = True)
#master = form_dict("master_quotes", quotes = True)

# A list and function for the picking of random races to tweet
races = [space_marine, eldar, imperial_guard, chaos]
def tweet_quote():
    race = random.choice(races)
    if race == space_marine:
        addition = " From, an anonymous Astartes"
    elif race == chaos:
        addition = " From, an anonymous Heretic"
    elif race == eldar:
        addition = " From, an anonymous Eldar"
    else:
        addition = " From, an anonymous Guardsman"
    return('"' + markov_gen(race,random.randint(10,15)) + '"' + addition)

# Debugging --- uncomment as nessacery

#test_text_array = ["this", "is", "a", "small", "sentence", "to", "test", "the", "building", "of", "a", "markov", "chain", "generator"]
#test_text_string = "this is a small sentence to test the building of a markov chain generator"
#trip_list("space_marine_quotes", quotes = True)
#read_file_quotes("space_marine_quotes")
#print(read_file("test"))
#print(markov_gen("test", 5))
#print(markov_gen(test_text_string, 5))
#print(form_dict(test_text_array))
#print(list_triples(test_text_array))
#print(test_text_array)
