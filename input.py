import nltk
import os
import json
import nltk.corpus
import string
from textblob import TextBlob


AWARD_CATEGORY_NAMES = ['Best Motion Picture – Drama',
'Best Motion Picture – Musical or Comedy',
'Best Motion Picture – Foreign Language',
'Best Motion Picture – Animated',
'Best Director – Motion Picture',
'Best Actor in a Motion Picture – Drama',
'Best Actor in a Motion Picture – Musical or Comedy',
'Best Actress in a Motion Picture – Drama',
'Best Actress in a Motion Picture – Musical or Comedy',
'Best Supporting Actor – Motion Picture',
'Best Supporting Actress – Motion Picture',
'Best Screenplay – Motion Picture',
'Best Original Score – Motion Picture',
'Best Original Song – Motion Picture',
'Cecil B. DeMille Award for Lifetime Achievement in Motion Pictures',
'Best Television Series – Drama',
'Best Television Series – Musical or Comedy',
'Best Miniseries or Motion Picture – Television',
'Best Actor in a Television Series – Drama',
'Best Actor in a Television Series – Musical or Comedy',
'Best Actor in a Miniseries or Motion Picture – Television',
'Best Actress in a Television Series – Drama',
'Best Actress in a Television Series – Musical or Comedy',
'Best Actress in a Miniseries or Motion Picture – Television',
'Best Supporting Actor in a Series, Miniseries or Motion Picture – Television',
'Best Supporting Actress in a Series, Miniseries or Motion Picture – Television',
'Carol Burnett Award for Lifetime Achievement in Television']

AWARD_CATEGORY_NAMES_LOWERED = [x.lower() for x in AWARD_CATEGORY_NAMES]

def loadTweet(filename):
    file = open(filename)
    raw_json = json.load(file)
    tweets = []
    for item in raw_json:
        tweets.append(item['text'])
    return tweets[0]



# process text, return word dict and sentiment of tweet
def parseTweet(tweet):
    tokens = nltk.word_tokenize(tweet.text)
    # words list to dict with qty of words

def lowerTweet(tweet):
    return tweet.lower()    

def findIndexOfWord(tweet, word):
    return tweet.lower().split().index(word)

def removePunctuation(tweet):
    return tweet.translate(str.maketrans('', '', string.punctuation))

print(loadTweet('gg2013.json'))
print(findIndexOfWord(loadTweet('gg2013.json'), 'dress!'))
print(lowerTweet(removePunctuation(loadTweet('gg2013.json'))))
