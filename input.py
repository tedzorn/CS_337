import json
#import nltk

def loadTweet(filename):
    file = open(filename)
    raw_json = json.load(file)
    tweets = []
    for item in raw_json:
        tweets.append(item['text'])
    print(tweets[0])



# process text, return word dict and sentiment of tweet
def parseTweet(tweet):
    tokens = nltk.word_tokenize(tweet.text)
    # words list to dict with qty of words

loadTweet('gg2013.json')